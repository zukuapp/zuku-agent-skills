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

![version](https://img.shields.io/badge/version-v27.26102701-informational)

## Overview

This repository contains original Agent Skills for the ZUKU public HTTP API and for JUMP game presentation across screens, input methods and assistive technology.

| Skill | Use |
| --- | --- |
| [zuku-public-api](skills/zuku-public-api/SKILL.md) | Public v1 content reads, response/error handling, package manifests, content-scoped Cloud contracts |
| [zuku-game-integration](skills/zuku-game-integration/SKILL.md) | Ren'Py, Phaser, PixiJS, Godot and Ruffle exports, relative assets, sandbox playback, package versus publication evidence |
| [zuku-game-accessibility](skills/zuku-game-accessibility/SKILL.md) | Responsive presentation, readable text, keyboard/touch controls, reduced motion, semantic transcript design |

## Requirements

- An agent that loads skills from a skills directory (for example, Codex).
- Python 3 for the helper and validation scripts. The scripts use only the standard library.

## Install

1. Copy the required `skills/<name>` folders to the agent's skills directory. The Codex default is `~/.codex/skills/`.
2. If the Codex skill installer is present, run:

   ```text
   $skill-installer install zuku-public-api, zuku-game-integration and zuku-game-accessibility from zukuapp/zuku-agent-skills
   ```

3. Start a new turn. The agent loads installed skills on the next turn.

## Usage

The following command reads one public game record and needs no credentials:

```sh
python3 skills/zuku-public-api/scripts/check_public_content.py cnt_e03f90d34e1a4fd59c55f5582948af1d
```

Output shape: `{"status":200,"id":"cnt_...","category":"jump","type":"game","title":"..."}`.

API reference: [ZUKU API docs](https://www.zuzunza.com/docs/api). Live docs and the project's pinned engine version take precedence over the examples.

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Report documentation drift with the observed public endpoint and a redacted response shape. Do not submit credentials or private records.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Original skills and helper code are licensed under Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
