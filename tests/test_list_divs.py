import pytest

from sitecheck.list_divs import list_div_attribs, print_div_attribs


# Test data for list_div_attribs
@pytest.mark.parametrize(
    "html, attrib, expected",
    [
        # Test case 1: Happy path, multiple divs with classes and ids
        (
            '<div class="test" id="div1"></div><div class="test2" id="div2"></div>',
            "class",
            [["test"], ["test2"]],
        ),
        # Test case 2: Happy path, single div with class
        (
            '<div class="test"></div>',
            "class",
            [["test"]],
        ),
        # Test case 3: Edge case, no divs
        (
            '<p class="test"></p>',
            "class",
            [],
        ),
        # Test case 4: Edge case, divs without the specified attribute
        (
            '<div id="div1"></div><div id="div2"></div>',
            "class",
            [],
        ),
    ],
    ids=["multiple_divs", "single_div", "no_divs", "no_attrib"],
)
def test_list_div_attribs(html, attrib, expected):
    # Act
    result = list_div_attribs(html, attrib)

    # Assert
    assert result == expected


# Test data for print_div_attribs
@pytest.mark.parametrize(
    "html, attrib, expected_output",
    [
        # Test case 1: Happy path, multiple divs with classes and ids
        (
            '<div class="test" id="div1"></div><div class="test2" id="div2"></div>',
            "class",
            "Found 2 named div classes.\n['test']\n['test2']\n",
        ),
        # Test case 2: Happy path, single div with class
        (
            '<div class="test"></div>',
            "class",
            "Found 1 named div classes.\n['test']\n",
        ),
        # Test case 3: Edge case, no divs
        (
            '<p class="test"></p>',
            "class",
            "Found 0 named div classes.\n",
        ),
        # Test case 4: Edge case, divs without the specified attribute
        (
            '<div id="div1"></div><div id="div2"></div>',
            "class",
            "Found 0 named div classes.\n",
        ),
    ],
    ids=["multiple_divs", "single_div", "no_divs", "no_attrib"],
)
def test_print_div_attribs(capsys, html, attrib, expected_output):
    # Act
    print_div_attribs(html, attrib)

    # Assert
    captured = capsys.readouterr()
    assert captured.out == expected_output
