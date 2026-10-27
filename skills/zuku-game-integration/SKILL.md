---
name: zuku-game-integration
description: Export and integrate Ren'Py, Phaser, PixiJS, Godot or Ruffle games with ZUKU JUMP packaging, sandboxed playback and the actual Game Cloud contracts.
---

# ZUKU game integration

Preserve the requested game, engine and narrative. Pick the smallest engine-specific reference from [engines.md](references/engines.md); verify the project's pinned engine version before copying API examples. Use `zuku-public-api` for ZUKU content and Cloud contracts, and `zuku-game-accessibility` when changing presentation or input.

Treat source, exported package, admitted package and published content as distinct artifacts. Keep package-relative asset/module paths valid. Inspect the manifest and actual playable entry rather than assuming a ZIP is runnable. A server response or host ready phase does not prove a completed game frame. Establish meaningful evidence of input, progress/completion and restart; report missing runtime checks honestly when browsers are prohibited.

ZUKU game-kit provides core, arcade, RPG, VN and story modules plus Game Cloud. Check the deployed module before using it. Cloud consent/account state belongs to the trusted host, not the game canvas.

For a stalled game, compare package metadata, requested asset status, engine initialization and visible progress. Distinguish a short manifest-fetch deadline from the larger WASM startup deadline. Fix the identified export/runtime contract; do not bypass ticket binding, origin isolation or owner publication checks.

Publish an owner-scoped draft or replace a game package only when the user's request authorizes it. Preserve title/content ID, existing progress semantics, story/artwork and licenses when repairing an existing game. Keep a recoverable previous package until the replacement is verified.
