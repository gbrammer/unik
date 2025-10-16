#!/usr/bin/env python3
"""
Example usage of the unik package.
Run this script to see how to use the unik functions.
"""

from unik import unique, unique_count, is_unique


def main():
    """Demonstrate the unik package functionality."""
    print("=" * 60)
    print("unik - Helper for unique entries in lists / arrays")
    print("=" * 60)
    print()

    # Example 1: Basic unique function
    print("Example 1: Get unique items from a list")
    items = [1, 2, 2, 3, 1, 4, 3, 5]
    print(f"Original list: {items}")
    print(f"Unique items (order preserved): {unique(items)}")
    print(f"Unique items (order not preserved): {unique(items, preserve_order=False)}")
    print()

    # Example 2: Unique with strings
    print("Example 2: Get unique items from a string list")
    words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
    print(f"Original list: {words}")
    print(f"Unique items: {unique(words)}")
    print()

    # Example 3: Counting unique items
    print("Example 3: Count occurrences of unique items")
    numbers = [1, 2, 2, 3, 1, 4, 3, 1, 2]
    print(f"Original list: {numbers}")
    counts = unique_count(numbers)
    print(f"Item counts: {counts}")
    for item, count in counts.items():
        print(f"  {item} appears {count} time(s)")
    print()

    # Example 4: Check if list has all unique items
    print("Example 4: Check if all items are unique")
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 2, 3, 4]
    print(f"List 1: {list1}")
    print(f"All unique? {is_unique(list1)}")
    print(f"List 2: {list2}")
    print(f"All unique? {is_unique(list2)}")
    print()

    # Example 5: Working with different data types
    print("Example 5: Working with mixed data types")
    mixed = [1, '1', 2, '2', 1, 2]
    print(f"Original list: {mixed}")
    print(f"Unique items: {unique(mixed)}")
    print(f"Item counts: {unique_count(mixed)}")
    print()

    print("=" * 60)
    print("For more information, visit: https://github.com/gbrammer/unik")
    print("=" * 60)


if __name__ == "__main__":
    main()
