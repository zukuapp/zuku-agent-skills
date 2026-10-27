# Observed public contracts

Baseline: ZUKU v1 docs as of 2026-10-02. Public docs: https://www.zuzunza.com/docs/api/getting-started, https://www.zuzunza.com/docs/api/contents, https://www.zuzunza.com/docs/api/media, https://www.zuzunza.com/docs/api/game-cloud.

## Envelopes and content

Successful JSON uses `{success:true,data,meta}`; errors use `{success:false,error:{code,message},meta}`. A successful public content read is `GET /api/v1/contents/{id}` with `data.content`. Content includes `id`, `category`, `type`, `title`, `description`, creator, media metadata and statistics. Public JUMP content has category `jump`, type `game`. Drafts require owner authorization; anonymous unavailable content returns 404. Some deletion responses have no body (204). Do not depend on a static rate-limit header as measured remaining capacity.

Example, inside a trusted ZUKU page:

```js
async function getPublicContent(id) {
  const response = await fetch(`/api/v1/contents/${encodeURIComponent(id)}`, {
    headers: {Accept: 'application/json'}, signal: AbortSignal.timeout(10000),
  });
  const result = await response.json();
  if (!response.ok || !result.success) {
    throw Object.assign(new Error(result.error?.message || `HTTP ${response.status}`),
      {status: response.status, code: result.error?.code});
  }
  return result.data.content;
}
```

## JUMP playback

`GET /api/v1/jump/games/{id}/package-manifest` returns `data.content_id`, `entry_point`, `play_base` and files with path, byte size and SHA-256. The current host accepts the content-bound `/api/v1/jump/games/{id}/play/{ticket}/` prefix; the 32-hex ticket is ephemeral and must not be stored as a permanent public asset URL. Validate the entry path (no traversal, backslashes, control characters or URL delimiters). Resolve package assets relative to the returned play base.

The HTML5 player runs scripts in an opaque-origin sandbox. Its current allowed capabilities are scripts, pointer lock, fullscreen, gamepad and autoplay; account credentials and privileged device APIs are excluded. IndexedDB/localStorage assumptions can fail there. A large WASM document can take longer than metadata; metadata fetch timeout and game startup timeout are separate. Host phase `playing` is not sufficient evidence that engine assets finished or input works.

The host's `zuku-html5` v1 ready/error messages are session-bound and source-frame checked. Do not loosen the sandbox or origin checks to fix an export. Audit the export's CSP/module/asset requirements instead.

## Game Cloud

The deployed game-kit exports `GameCloud` and `watchGameCloudAuth`. Inside a JUMP HTML5/ZWF frame it uses a session-bound `zuku-game-cloud` version-1 message bridge; outside the frame the SDK calls POST `/api/v1/cloud/runtime/{contentId}/{action}` using a short-lived token provider. Do not put developer keys in packages.

```js
// Use the game-kit module supplied by your host/export, not an invented npm SDK.
const cloud = new GameCloud();
await cloud.connect(); // site-owned consent, or reuse signed-in consent
const board = await cloud.call('scores-list', {offset: 0});
```

Supported actions: `context`, `consent-revoke`, `scores-list`, `scores-submit`, `save`, `load`, `room-create`, `room-join`, `room-sync`, `room-leave`, `room-start`. Read current payload fields from the official Game Cloud page and your deployed SDK before writing a request. `connect({interactive:false})` can return `CONSENT_REQUIRED` or `UNAUTHORIZED`. `watchGameCloudAuth` is a notification to discard stale account UI and reconnect; unsubscribe on teardown. Never submit an old player's in-progress score under a newly connected player.

Scores are casual client-reported maxima, not authoritative competitive results. Shared-state rooms allow 2–8 authenticated players; poll at 500–1000 ms, increment `seq`, keep state below 4 KB, and implement prediction separately. Rooms are not an authoritative high-frequency physics server.
