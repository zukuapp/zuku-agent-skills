# Primary engine references

These are sources to consult for the installed version, not dependencies automatically added to a project. Examples belong to their upstream licenses; this skill contains original guidance and does not bundle engine code.

| Engine | Repository / API | ZUKU integration concern |
| --- | --- | --- |
| Ren'Py | https://github.com/renpy/renpy · https://www.renpy.org/doc/html/web.html · https://www.renpy.org/doc/html/self_voicing.html | Large WASM startup, opaque-origin persistence limits, export asset paths, keyboard/touch and accessible dialogue. Keep engine copyright and required third-party notices in the export. |
| Phaser | https://github.com/phaserjs/phaser · https://docs.phaser.io/ | Pin the actual major version; use its scale/input APIs. Keep semantic DOM controls around a canvas when canvas controls cannot expose names/state. |
| PixiJS | https://github.com/pixijs/pixijs · https://pixijs.com/8.x/guides/components/accessibility | Accessibility needs the relevant plugin/DOM layer and meaningful labels; rendering alone does not produce semantic controls. |
| Godot | https://github.com/godotengine/godot · https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html | Validate web-export threading/isolation, audio unlock and renderer requirements against the sandbox. Native exports are not interchangeable with web packages. |
| Ruffle | https://github.com/ruffle-rs/ruffle · https://ruffle.rs/ | Preserve source SWF and use reviewed runtime paths; report ActionScript compatibility gaps rather than claiming every SWF works. |
| Gamepad | https://www.w3.org/TR/gamepad/ | Keep keyboard/pointer alternatives, dead zones and remapping; API availability is not proof a controller was physically tested. |

Use optional engine extensions only when a concrete requirement justifies them. Keep both engine version and source provenance in the release record.
