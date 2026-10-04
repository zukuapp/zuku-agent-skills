<!-- BEGIN ZUKU OFFICIAL BRAND -->
<!-- markdownlint-disable MD033 MD041 -->
<p align="center">
  <a href="https://docs.zuzunza.com/">
    <picture>
      <source media="(prefers-color-scheme: dark)"
        srcset="docs/branding/zuku-logo-dark.png">
      <img src="docs/branding/zuku-logo-light.png"
        alt="ZUKU" width="320">
    </picture>
  </a>
</p>
<p align="center">ZUKU - 내가 불러 일으키는 새로운 창작.</p>
<!-- markdownlint-enable MD033 MD041 -->
<!-- END ZUKU OFFICIAL BRAND -->

# ZUKU API and game skills

Original Agent Skills for integrating the ZUKU public HTTP API and making JUMP games usable across screens, input methods and assistive technology. They document actual content/package/Game Cloud boundaries and connect them to primary Ren'Py, Phaser, PixiJS, Godot and Ruffle references.

## Skills

| Skill | Use |
| --- | --- |
| [zuku-public-api](skills/zuku-public-api/SKILL.md) | Public v1 content reads, response/error handling, package manifests, content-scoped Cloud contracts |
| [zuku-game-integration](skills/zuku-game-integration/SKILL.md) | Engine exports, relative assets, sandbox playback, package versus publication evidence |
| [zuku-game-accessibility](skills/zuku-game-accessibility/SKILL.md) | Responsive presentation, readable text, keyboard/touch controls, reduced motion, semantic transcript design |

These skills do not contain deployment credentials, private infrastructure configuration or game source/artwork. Installing a skill does not authorize uploads, payments or publication.

## Install

Copy the desired `skills/<name>` folders to your agent's skills directory. For Codex, the default is `~/.codex/skills/`. If Codex's skill installer is available:

```text
$skill-installer install zuku-public-api, zuku-game-integration and zuku-game-accessibility from zukuapp/zuku-agent-skills
```

The skills are available on the next turn after installation. Read only the skill and references relevant to the task.

## Example

Read a public game record without credentials or mutations:

```sh
python3 skills/zuku-public-api/scripts/check_public_content.py cnt_e03f90d34e1a4fd59c55f5582948af1d
```

Expected shape: `{"status":200,"id":"cnt_...","category":"jump","type":"game","title":"..."}`. This proves only a public metadata read; it does not prove game runtime, authenticated writes or owner access.

API references: [ZUKU API docs](https://www.zuzunza.com/docs/api). Contract baseline: 2026-10-02; check live docs and the actual pinned engine version when using examples.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Report documentation drift with the observed public endpoint and a redacted response shape. Do not submit credentials or private records.

## License

Original skills and helper code are licensed under Apache-2.0. Upstream engines, third-party installed skills, game artwork and ZUKU platform implementation retain their own licenses and are not included here. See [NOTICE](NOTICE).
