import pytest

from sitecheck.extract_div import extract_div

# Test cases for the happy path, edge cases, and error cases
test_cases = [
    # Happy path tests
    ("happy1", "<div class='test'>Hello World</div>", "test", "Hello World"),
    ("happy2", "<div class='foo'>Foo Bar</div>", "foo", "Foo Bar"),
    ("happy3", "<div class='empty'></div>", "empty", ""),
    # Edge case tests
    (
        "edge1",
        "<div class='test'><p>Some text</p></div>",
        "test",
        "<p>Some text</p>",
    ),  # div with nested elements
    # Error case tests
    (
        "error1",
        "<div class='test'>Hello World</div>",
        "nonexistent",
        None,
    ),  # nonexistent div class
    ("error2", "", "test", None),  # empty HTML
    ("error3", "Not HTML", "test", None),  # non-HTML input
]


@pytest.mark.parametrize("test_id,html,div_class,expected", test_cases)
def test_extract_div(test_id, html, div_class, expected):
    # Arrange
    # No arrangement necessary as all inputs are provided via test parameters

    # Act
    result = extract_div(html, div_class)

    # Assert
    assert result == expected
