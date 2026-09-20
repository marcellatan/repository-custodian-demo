# Troubleshooting

## Tests Do Not Run

Make sure Python is installed and pytest is available.

Run:

```bash
pytest
```

If pytest is not installed:

```bash
pip install pytest
```

## Import Errors

Run the tests from the root directory of the repository.

The expected repository structure is:

```text
repository-custodian-demo/
├── src/
│   └── simple_app.py
└── tests/
    └── test_simple_app.py
```

## Invalid Temperature Unit

The conversion function supports:

* `C` for Celsius
* `F` for Fahrenheit

Other units will result in a validation error.

## Empty Temperature Values

A missing temperature value is considered invalid and raises a `ValueError`.

## Reporting a New Problem

If a problem cannot be resolved using this guide, create a GitHub issue with:

1. A description of the problem.
2. Steps to reproduce it.
3. Expected behaviour.
4. Actual behaviour.
5. Relevant error messages.
