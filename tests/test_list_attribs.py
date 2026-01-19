import pytest
from bs4 import BeautifulSoup

from sitecheck.list_attribs import find_attribs, find_elements


# Test cases for find_elements function
@pytest.mark.parametrize(
    "html,element,expected_result,test_id",
    [
        # Edge cases
        ("", "p", [], "edge_case_1"),  # Empty HTML
        ("<p>Hello</p>", "", [], "edge_case_2"),  # Empty element
        # Error cases
        ("<p>Hello</p>", "div", [], "error_case_1"),  # Element not found
    ],
)
def test_find_elements(html, element, expected_result, test_id):
    # Arrange - omitted as all input values are provided via the test parameters

    # Act
    result = find_elements(html, element)

    # Assert
    assert result == expected_result, f"Test case {test_id} failed"


# Test cases for find_attribs function
@pytest.mark.parametrize(
    "elements,attrib,expected_result,test_id",
    [
        # Happy path tests
        (
            [BeautifulSoup("<p class='test'>Hello</p>", "html.parser").p],
            "class",
            [["test"]],
            "happy_path_1",
        ),
        (
            [BeautifulSoup("<p id='test'>Hello</p>", "html.parser").p],
            "id",
            ["test"],
            "happy_path_2",
        ),
        # Edge cases
        ([], "class", [], "edge_case_1"),  # Empty elements
        (
            [BeautifulSoup("<p class='test'>Hello</p>", "html.parser").p],
            "",
            [],
            "edge_case_2",
        ),  # Empty attribute
        # Error cases
        (
            [BeautifulSoup("<p>Hello</p>", "html.parser").p],
            "class",
            [],
            "error_case_1",
        ),  # Attribute not found
    ],
)
def test_find_attribs(elements, attrib, expected_result, test_id):
    # Arrange - omitted as all input values are provided via the test parameters

    # Act
    result = find_attribs(elements, attrib)

    # Assert
    assert result == expected_result, f"Test case {test_id} failed"
