"""Example test module.

This module demonstrates how to write tests using pytest.

Run tests with:
    mise run test
    # or
    pytest tests -vv
"""

from pathlib import Path

import pytest


def test_example_basic() -> None:
    """Test basic Python functionality."""
    assert 1 + 1 == 2
    assert "hello" == "hello"
    assert True is True


def test_example_with_fixture(tmp_path: Path) -> None:
    """Test using pytest fixtures.

    Args:
        tmp_path: Pytest fixture providing a temporary directory
    """
    # Create a temporary file
    test_file = tmp_path / "test.txt"
    test_file.write_text("Hello, World!")

    # Read and verify
    content = test_file.read_text()
    assert content == "Hello, World!"
    assert test_file.exists()


def test_example_list_operations() -> None:
    """Test list operations."""
    numbers = [1, 2, 3, 4, 5]

    assert len(numbers) == 5
    assert numbers[0] == 1
    assert numbers[-1] == 5
    assert sum(numbers) == 15


def test_example_dict_operations() -> None:
    """Test dictionary operations."""
    data = {"name": "Alice", "age": 30}

    assert data["name"] == "Alice"
    assert data.get("age") == 30
    assert "name" in data
    assert "email" not in data


def test_example_exception() -> None:
    """Test exception handling."""
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0

    with pytest.raises(KeyError):
        data = {}
        _ = data["nonexistent_key"]


@pytest.mark.parametrize(
    "input_value,expected",
    [
        (0, 0),
        (1, 1),
        (2, 4),
        (3, 9),
        (-2, 4),
    ],
)
def test_example_parametrized(input_value: int, expected: int) -> None:
    """Test using parametrize decorator.

    Args:
        input_value: Input to square
        expected: Expected result
    """
    result = input_value**2
    assert result == expected


class TestExampleClass:
    """Example test class grouping related tests."""

    def test_string_upper(self) -> None:
        """Test string upper method."""
        assert "hello".upper() == "HELLO"

    def test_string_lower(self) -> None:
        """Test string lower method."""
        assert "WORLD".lower() == "world"

    def test_string_strip(self) -> None:
        """Test string strip method."""
        assert "  spaces  ".strip() == "spaces"


# Example of a test that will be skipped
@pytest.mark.skip(reason="Example of skipped test")
def test_example_skipped() -> None:
    """This test will be skipped."""
    raise AssertionError("This won't be executed")


# Example of conditional skip
@pytest.mark.skipif(Path("/nonexistent/path").exists(), reason="Only run if path doesn't exist")
def test_example_conditional_skip() -> None:
    """This test runs conditionally."""
    assert True
