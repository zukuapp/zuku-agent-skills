# Contributing

Keep skill entrypoints concise and task-specific. Put conditional detail in references, document public contract changes with primary-source links, and preserve authorization boundaries. New helpers should be bounded, credential-free by default, and have a reproducible lightweight check.

Run `python3 scripts/validate.py` before opening a pull request. A public GET smoke check is optional and network-dependent; runtime or screen-reader behavior must be reported separately from static validation. Do not add heavy browser/build jobs to the default validation.

Use placeholders for IDs and tokens in authenticated examples. Never commit credentials, customer data, private service paths or copied production logs. Retain upstream license notices for any permitted imported material.
