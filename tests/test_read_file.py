import pytest

from sitecheck.read_file import read_file

# Test cases: (file_content, expected_result, raises_error)
test_cases = [
    ("Hello, World!", "Hello, World!", False, "happy_path_simple_string"),
    ("", "", False, "edge_case_empty_file"),
    (
        "Special characters: äöüß€",
        "Special characters: äöüß€",
        False,
        "happy_path_special_characters",
    ),
    (None, None, True, "error_case_no_file"),
]


@pytest.mark.parametrize(
    "file_content,expected_result,raises_error,test_id",
    test_cases,
    ids=[tc[-1] for tc in test_cases],
)
def test_read_file(file_content, expected_result, raises_error, test_id, tmp_path):
    # Arrange
    if file_content is not None:
        file_path = tmp_path / "test.txt"
        file_path.write_text(file_content, encoding="utf-8")
    else:
        file_path = tmp_path / "non_existent_file.txt"

    # Act
    if raises_error:
        with pytest.raises(FileNotFoundError):
            read_file(file_path)
    else:
        result = read_file(file_path)

        # Assert
        assert result == expected_result
