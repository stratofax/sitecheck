import pytest

from sitecheck.remove_element import remove_element

# Test cases for the happy path, edge cases, and error cases
test_cases = [
    # Happy path tests
    {
        "id": "happy_path_1",
        "html": "<html><body><p>Hello World</p></body></html>",
        "elements": ["p"],
        "expected": "<html><body></body></html>",
    },
    {
        "id": "happy_path_2",
        "html": "<html><body><div><p>Hello World</p></div></body></html>",
        "elements": ["div"],
        "expected": "<html><body></body></html>",
    },
    # Edge case tests
    {
        "id": "edge_case_1",
        "html": "<html><body><p>Hello World</p></body></html>",
        "elements": [],
        "expected": "<html><body><p>Hello World</p></body></html>",
    },
    {
        "id": "edge_case_2",
        "html": "",
        "elements": ["p"],
        "expected": "",
    },
    # Error case tests
    {
        "id": "error_case_1",
        "html": "<html><body><p>Hello World</p></body></html>",
        "elements": ["nonexistent"],
        "expected": "<html><body><p>Hello World</p></body></html>",
    },
]


@pytest.mark.parametrize("test_case", test_cases, ids=[tc["id"] for tc in test_cases])
def test_remove_element(test_case):
    # Arrange
    html = test_case["html"]
    elements = test_case["elements"]

    # Act
    result = remove_element(html, elements)

    # Assert
    assert result == test_case["expected"]
