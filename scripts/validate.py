#!/usr/bin/env python3
"""Validate distributable skills without network, browsers or third-party packages."""
import ast
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected = {'zuku-public-api', 'zuku-game-integration', 'zuku-game-accessibility'}
skills = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
assert skills == expected, 'unexpected skill inventory'
checked = 0
for name in sorted(skills):
    folder = root / 'skills' / name
    content = (folder / 'SKILL.md').read_text()
    match = re.match(r'^---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n', content)
    assert match and match[1] == name and len(match[2]) > 20, 'invalid skill metadata'
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if not target.startswith(('https://', 'http://')):
            assert (folder / target).is_file(), 'missing local reference: ' + target
    for path in folder.rglob('*.py'):
        ast.parse(path.read_text(), filename=str(path))
    checked += 1
for path in root.rglob('*'):
    if not path.is_file() or '.git' in path.parts:
        continue
    raw = path.read_text(errors='strict')
    assert not re.search(r'(?:ghp_|github_pat_|sk_live_)[A-Za-z0-9_]{16,}', raw), 'credential-like material found'
    assert not re.search(r'^-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----$', raw, re.M), 'private key material found'
print(f'Validated {checked} skills, local references, Python syntax and basic secret exclusions.')
