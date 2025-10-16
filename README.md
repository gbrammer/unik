# unik

Helper for unique entries in lists / arrays

## Installation

You can install unik using pip:

```bash
pip install unik
```

## Usage

```python
from unik import unique, unique_count, is_unique

# Get unique items from a list (preserving order)
items = [1, 2, 2, 3, 1, 4]
print(unique(items))  # [1, 2, 3, 4]

# Get unique items without preserving order (faster)
print(unique(items, preserve_order=False))  # [1, 2, 3, 4] (order may vary)

# Count occurrences of unique items
print(unique_count(items))  # {1: 2, 2: 2, 3: 1, 4: 1}

# Check if all items are unique
print(is_unique([1, 2, 3]))  # True
print(is_unique([1, 2, 2]))  # False
```

## Features

- **`unique(items, preserve_order=True)`**: Returns a list of unique items
  - `preserve_order=True` (default): Preserves the order of first occurrence
  - `preserve_order=False`: Uses set for faster operation (order not guaranteed)

- **`unique_count(items)`**: Returns a dictionary with items as keys and their counts as values

- **`is_unique(items)`**: Returns `True` if all items in the list are unique, `False` otherwise

## Development

To install for development:

```bash
git clone https://github.com/gbrammer/unik.git
cd unik
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Build the package:

```bash
python -m build
```

## License

MIT License - see LICENSE file for details
