---
name: zuku-public-api
description: Integrate with ZUKU's public v1 HTTP API, anonymous content reads, JUMP package manifests, and content-scoped Game Cloud using documented contracts.
---

# ZUKU public API

Start with the smallest API surface the requested product needs. Read [contracts.md](references/contracts.md) for public reads, package playback, response envelopes and Game Cloud. Follow the live documentation at https://www.zuzunza.com/docs/api when a contract changes; a local sample is a dated observation, not a permanent guarantee.

Use `/api/v1` on the trusted site's origin, or `https://zuzunza.com/api/v1` for standalone public reads. Preserve HTTP status and API error code, handle empty 204 responses, bound response sizes and timeouts, and treat 429 as an actual rate-limit signal. Avoid inventing SDK methods or extrapolating authorization from a successful anonymous GET.

Keep account/developer credentials on the trusted host or server. A JUMP game iframe uses the content-scoped bridge; it must not receive the site's bearer token. Consent is presented by the site. Authenticated mutations, uploads, publication and paid Cloud operations need the user's task authorization and their actual owner-scoped account context.

For a read-only smoke check, run `python3 scripts/check_public_content.py CONTENT_ID`; the helper fetches one public record, prints only a compact metadata summary, and never reads credentials. It does not validate game runtime, authenticated writes or console ownership.
