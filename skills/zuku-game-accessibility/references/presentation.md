# Presentation and accessible game output

Primary guidance: https://www.w3.org/WAI/WCAG22/quickref/ ; Ren'Py self-voicing https://www.renpy.org/doc/html/self_voicing.html ; PixiJS accessibility https://pixijs.com/8.x/guides/components/accessibility.

## Player-facing acceptance

- Dialogue fits a narrow portrait screen at the chosen large text setting; avoid clipping and dense four-column menus on mobile.
- Dialogue/background and focus/control contrasts remain legible. A solid high-contrast textbox can preserve art while improving reading.
- Tab focus is visible, menu/back/pause/next actions have names and keyboard alternatives, and the player can leave a focused control/iframe without a trap.
- Touch targets allow deliberate input, with meaningful spacing; hover is not the sole way to discover actions.
- Reduced-motion mode disables nonessential transitions, shake and animated UI while preserving required progress feedback.
- Text speed and auto-advance can be changed or paused. Sound is optional for essential story/objective information.
- Semantic text follows the displayed speaker and line. A screen-reader mode can expose explicit next/back controls without relying on canvas coordinates.
- Pause/restart and scene navigation preserve intended save/progression behavior. State which preferences/saves survive a reload; sandboxed session memory is not durable storage.

## Optional transcript bridge design

This is an implementation design, not a pre-existing universal ZUKU API. Give any new protocol a separate channel/version and obtain its session binding from the host export contract. A receiving host must bind messages to the current content frame. For a sandboxed opaque origin, source-frame/session validation is essential; trusting `origin === 'null'` alone is insufficient.

Choose finite speaker/line/scene lengths, a finite number of actions, message-rate limits, and bounded transcript history. Discard stale messages after iframe replacement. Render text with `textContent` and never accept HTML/script/URL commands from dialogue. Use a polite live region for a completed line, with an option to disable announcements. Avoid replaying long history automatically; expose history behind a named user action.

Game-owned actions must be explicit allowed IDs. The host must not dispatch arbitrary keyboard scripts, URLs, credentials, network requests or privileged site actions from a transcript payload. Separate game text/control bridging from existing Game Cloud consent and authentication.

Inspect the engine's hooks for speaker/dialogue changes; do not scrape canvas pixels or infer dialogue by OCR. A bridge that receives state but cannot invoke the actual game action must not present a working next button. Check teardown, scene changes, repeat lines and stale sessions.
