"""
unik - Helper for unique entries in lists / arrays

A simple utility to work with unique elements in lists and arrays.
"""

__version__ = "0.1.0"
__author__ = "Gabe Brammer"
__license__ = "MIT"


def unique(items, preserve_order=True):
    """
    Return unique items from a list or iterable.
    
    Args:
        items: An iterable (list, tuple, etc.) to extract unique items from
        preserve_order: If True, preserve the order of first occurrence (default: True)
    
    Returns:
        A list containing unique items
        
    Examples:
        >>> unique([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
        
        >>> unique(['a', 'b', 'a', 'c'])
        ['a', 'b', 'c']
    """
    if preserve_order:
        seen = set()
        result = []
        for item in items:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    else:
        return list(set(items))


def unique_count(items):
    """
    Return a dictionary with unique items as keys and their counts as values.
    
    Args:
        items: An iterable (list, tuple, etc.) to count unique items from
    
    Returns:
        A dictionary mapping unique items to their counts
        
    Examples:
        >>> unique_count([1, 2, 2, 3, 1, 4])
        {1: 2, 2: 2, 3: 1, 4: 1}
    """
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def is_unique(items):
    """
    Check if all items in the list are unique.
    
    Args:
        items: An iterable (list, tuple, etc.) to check
    
    Returns:
        True if all items are unique, False otherwise
        
    Examples:
        >>> is_unique([1, 2, 3, 4])
        True
        
        >>> is_unique([1, 2, 2, 3])
        False
    """
    return len(items) == len(set(items))


__all__ = ['unique', 'unique_count', 'is_unique']
