# Contributing

## Guidelines

- Keep skill entrypoints concise and task-specific.
- Put conditional detail in references.
- Document public contract changes with primary-source links.
- Preserve authorization boundaries.
- New helpers are bounded, credential-free by default and have a reproducible lightweight check.

## Pull requests

1. Run the validator:

   ```sh
   python3 scripts/validate.py
   ```

2. Report runtime or screen-reader results separately from static validation. A public GET smoke check is optional and requires network access.
3. Do not add heavy browser or build jobs to the default validation.

## Data handling

Use placeholders for IDs and tokens in authenticated examples. Never commit credentials, customer data, private service paths or copied production logs. Retain upstream license notices for any permitted imported material.
