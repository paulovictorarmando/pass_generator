<!--
Keep this README focused on: what it does, why it’s useful, how to run it, where to get help, and how to contribute.
-->

# pass_generator

A small Python password generator with an interactive CLI.

It asks you for a desired password length and prints a randomly generated password. Lengths below 10 are automatically bumped to 10.

## Why this is useful

- Zero dependencies (Python standard library only)
- Quick interactive usage via a simple CLI
- Reusable generator function (`pass_generator.generator`) for scripting
- Enforces a minimum password length of 10 characters

## Getting started

### Requirements

- Python 3.x (no third‑party packages required)

### Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd pass_generator
```

### Run the CLI

```bash
python3 main.py
```

You’ll be prompted:

```text
Size(>9): 16
Pass: 0m8'v^mO}kX`y2g#
```

Notes:

- If you enter a number smaller than `10`, the generator will use `10`.
- The current implementation prints the effective size before printing the password.
- `Ctrl+C` cleanly exits with “program closed”.

## Using as a library (local import)

If you’re running code from this repository folder (or have it on your `PYTHONPATH`), you can import the generator:

```python
import pass_generator

password = pass_generator.generator(20)
print(password)
```

## Project layout

- [main.py](main.py): Interactive CLI entrypoint
- [pass_generator.py](pass_generator.py): Password generation logic
- [__init__.py](__init__.py): Marks the folder as a Python package (currently empty)

## Security note

This project uses Python’s `random` module. That’s fine for demos and casual use, but it is not intended for generating high-security passwords. If you need cryptographically strong randomness, consider switching the implementation to the `secrets` module.

## Getting help

- Check the source in [pass_generator.py](pass_generator.py) and [main.py](main.py)
- If you’re using this on GitHub, open an Issue in the repository describing:
	- your OS + Python version
	- what you ran
	- what you expected vs what happened

## Maintainers and contributing

- Maintainer: (add your name / handle here)
- Contributions: Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the quick process.


