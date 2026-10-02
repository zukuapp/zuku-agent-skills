---
name: zuku-game-accessibility
description: Improve ZUKU game presentation and accessibility across responsive screens, readable dialogue, keyboard/touch controls, reduced motion, and semantic screen-reader output.
---

# ZUKU game accessibility

Start from visible player needs: reading dialogue, discovering controls, moving through menus, pausing, and resuming. Preserve game content and progression. Apply the relevant engine's official accessibility API, then address gaps in the exported canvas experience. Read [presentation.md](references/presentation.md) for concrete acceptance and transcript-bridge design.

Give text scalable size and a contrast/solid-background option; keep controls and focus usable on portrait and landscape screens. Support keyboard, pointer and touch without a single-gesture-only action. Allow reduced transitions/animation, text speed adjustment and pausing auto-advance. Preferences must have honest persistence semantics when the game runs in an opaque-origin iframe.

Canvas pixels alone do not expose dialogue or control semantics. Prefer engine-supported accessibility; if needed add a bounded DOM transcript and real DOM controls synchronized to game state. Describe speaker, current dialogue, scene context and actual available actions. Avoid announcing entire story spoilers or every animation frame. Any cross-frame bridge must validate its known source frame, protocol version/session, message shape and bounds, and render user content with textContent.

Use WCAG guidance for the surrounding web controls and dialogue alternatives. Do not claim formal compliance or physical-device/screen-reader support solely from static checks. When runtime/browser work is prohibited, validate contracts and export structure with lightweight checks, label interaction checks unverified, and stop resource-heavy tooling.
