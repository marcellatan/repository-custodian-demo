# Repository Custodian Demo

A small GitHub repository used to demonstrate an AI-powered Repository Custodian for CAB432 Assessment 2.

## Project Overview

This project contains a simple temperature conversion application. The application supports:

* Celsius to Fahrenheit conversion
* Fahrenheit to Celsius conversion
* Basic input validation
* Automated tests

The repository is intentionally small so that the Repository Custodian can focus on repository monitoring, issue triage, documentation maintenance, and retrieval-augmented reasoning.

## Project Structure

```text
repository-custodian-demo/
├── README.md
├── CONTRIBUTING.md
├── docs/
│   ├── architecture.md
│   └── troubleshooting.md
├── src/
│   └── simple_app.py
└── tests/
    └── test_simple_app.py
```

## Running the Application

The conversion functions can be imported from `src.simple_app`.

Example:

```python
from src.simple_app import convert_temperature

result = convert_temperature(100, "C")
print(result)
```

Expected output:

```text
212.0
```

## Running Tests

Install pytest if required:

```bash
pip install pytest
```

Run the tests:

```bash
pytest
```

## Repository Custodian

This repository is used as the target repository for an AI-powered Repository Custodian.

The Repository Custodian is intended to:

1. Monitor repository issues.
2. Retrieve relevant repository context.
3. Summarise and triage issues.
4. Identify potential documentation drift.
5. Provide comments or recommendations on relevant issues.
6. Perform scheduled repository health checks.

The AI system will use retrieval from a vector store rather than repeatedly processing the entire repository.

## Scope

The Repository Custodian is not intended to be a general-purpose software development agent. Its primary purpose is repository monitoring, issue understanding, documentation checking, and maintenance assistance.
