# unik Package Structure

This document describes the structure of the unik Python package.

## Project Structure

```
unik/
├── .github/
│   └── workflows/
│       ├── publish.yml           # Automated publishing to PyPI on release
│       └── python-package.yml    # CI/CD testing on multiple Python versions
├── tests/
│   ├── __init__.py
│   └── test_unik.py             # Comprehensive test suite
├── unik/
│   └── __init__.py              # Main package with unique(), unique_count(), is_unique()
├── .gitignore                   # Git ignore file
├── LICENSE                      # MIT License
├── MANIFEST.in                  # Specifies files to include in distribution
├── PUBLISH.md                   # Guide for publishing to PyPI
├── README.md                    # User-facing documentation
├── example.py                   # Example usage script
├── pyproject.toml              # Modern Python packaging configuration (PEP 621)
└── setup.py                    # Backwards compatibility
```

## Files Description

### Core Package Files

- **`unik/__init__.py`**: The main module containing three functions:
  - `unique(items, preserve_order=True)`: Returns unique items from a list
  - `unique_count(items)`: Returns a dictionary with items and their counts
  - `is_unique(items)`: Checks if all items in a list are unique

### Configuration Files

- **`pyproject.toml`**: Modern Python packaging configuration following PEP 621
  - Defines package metadata (name, version, author, etc.)
  - Specifies dependencies and optional dependencies
  - Configures the build system (setuptools)
  - Python version requirement: >=3.8

- **`setup.py`**: Minimal setup file for backwards compatibility with older tools

- **`MANIFEST.in`**: Specifies which files to include in the source distribution

### Testing

- **`tests/test_unik.py`**: Comprehensive test suite with 10 tests covering:
  - Order preservation
  - Different data types (integers, strings)
  - Edge cases (empty lists, single items)
  - All three main functions

### CI/CD

- **`.github/workflows/python-package.yml`**: Continuous Integration workflow
  - Tests on Python 3.8, 3.9, 3.10, 3.11, 3.12
  - Runs tests, builds package, and checks with twine
  - Triggers on push and pull request to main branch

- **`.github/workflows/publish.yml`**: Automated publishing workflow
  - Builds and publishes to PyPI on release
  - Uses trusted publishing (no credentials needed)
  - Triggers when a GitHub release is created

### Documentation

- **`README.md`**: User-facing documentation with:
  - Installation instructions
  - Usage examples
  - Feature descriptions
  - Development setup guide

- **`PUBLISH.md`**: Detailed guide for publishing to PyPI
  - Step-by-step instructions
  - TestPyPI testing workflow
  - Authentication methods
  - Version update checklist

- **`example.py`**: Executable script demonstrating all features
  - Can be run directly to see examples
  - Shows different use cases and data types

## Development Workflow

### Setting Up for Development

```bash
git clone https://github.com/gbrammer/unik.git
cd unik
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

### Building the Package

```bash
python -m build
```

### Publishing to PyPI

See `PUBLISH.md` for detailed instructions.

## Package Distribution

The package can be distributed in two formats:

1. **Source Distribution (`.tar.gz`)**: Contains all source files
2. **Wheel (`.whl`)**: Binary distribution for faster installation

Both are created by `python -m build` and stored in the `dist/` directory.

## Version Management

Version is specified in two places:
- `pyproject.toml`: `version = "0.1.0"`
- `unik/__init__.py`: `__version__ = "0.1.0"`

Both should be updated together when releasing a new version.

## Dependencies

### Runtime Dependencies
- None! The package uses only Python standard library.

### Development Dependencies
- `pytest>=7.0`: For running tests
- `build>=0.10.0`: For building the package
- `twine>=4.0.0`: For uploading to PyPI

## Python Version Support

The package supports Python 3.8 and newer. This is specified in `pyproject.toml`:

```toml
requires-python = ">=3.8"
```

## License

MIT License - see LICENSE file for full text.
