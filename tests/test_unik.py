"""
Tests for the unik package.
"""
import pytest
from unik import unique, unique_count, is_unique


def test_unique_preserves_order():
    """Test that unique() preserves order by default."""
    result = unique([1, 2, 2, 3, 1, 4])
    assert result == [1, 2, 3, 4]


def test_unique_strings():
    """Test unique() with strings."""
    result = unique(['a', 'b', 'a', 'c'])
    assert result == ['a', 'b', 'c']


def test_unique_no_order():
    """Test unique() without order preservation."""
    result = unique([1, 2, 2, 3, 1, 4], preserve_order=False)
    assert set(result) == {1, 2, 3, 4}
    assert len(result) == 4


def test_unique_empty():
    """Test unique() with empty list."""
    result = unique([])
    assert result == []


def test_unique_count():
    """Test unique_count() returns correct counts."""
    result = unique_count([1, 2, 2, 3, 1, 4])
    assert result == {1: 2, 2: 2, 3: 1, 4: 1}


def test_unique_count_strings():
    """Test unique_count() with strings."""
    result = unique_count(['a', 'b', 'a', 'c', 'b', 'b'])
    assert result == {'a': 2, 'b': 3, 'c': 1}


def test_is_unique_true():
    """Test is_unique() returns True for unique items."""
    assert is_unique([1, 2, 3, 4]) is True


def test_is_unique_false():
    """Test is_unique() returns False for duplicate items."""
    assert is_unique([1, 2, 2, 3]) is False


def test_is_unique_empty():
    """Test is_unique() with empty list."""
    assert is_unique([]) is True


def test_is_unique_single():
    """Test is_unique() with single item."""
    assert is_unique([1]) is True
