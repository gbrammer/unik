# Quick Start Guide

## Installation

```bash
pip install unik
```

## Quick Reference

### Import
```python
from unik import unique, unique_count, is_unique
```

### Get Unique Items
```python
# Basic usage
unique([1, 2, 2, 3, 1, 4])  # Returns: [1, 2, 3, 4]

# Without order preservation (faster)
unique([1, 2, 2, 3, 1, 4], preserve_order=False)  # Returns: [1, 2, 3, 4]
```

### Count Unique Items
```python
unique_count([1, 2, 2, 3, 1, 4])  # Returns: {1: 2, 2: 2, 3: 1, 4: 1}
```

### Check if All Unique
```python
is_unique([1, 2, 3, 4])  # Returns: True
is_unique([1, 2, 2, 3])  # Returns: False
```

## Development Commands

```bash
# Install for development
pip install -e ".[dev]"

# Run tests
pytest

# Build package
python -m build

# Check package
twine check dist/*
```

## Publishing to PyPI

See `PUBLISH.md` for detailed instructions.

Quick version:
```bash
python -m build
twine upload dist/*
```
