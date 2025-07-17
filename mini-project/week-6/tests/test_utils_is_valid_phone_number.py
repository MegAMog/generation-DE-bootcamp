#Test utils/ utils.is_valid_phone_number function
from utils.utils import is_valid_phone_number 
import re, pytest


# scenario 1 - input data is a string and incl. only digits
def test_is_valid_phone_number_happy_path_digit():
    # Arrange
    input_data = '01234567891'
    expected = True, ""

    # Act
    result = is_valid_phone_number(input_data)

    # Assert
    assert result == expected


# scenario 2 - input data is a string and incl. letters
def test_is_valid_phone_number_happy_path_with_letters():
    # Arrange
    input_data = '012345678ml'
    expected = False, "Phone number must contain only digits."

    # Act
    result = is_valid_phone_number(input_data)

    # Assert
    assert result == expected


# scenario 3 - input data is a string and incl. only digits, but has wrong length
def test_is_valid_phone_number_happy_path_wrong_length():
    # Arrange
    input_data = '01'
    expected = False, "Phone number must be exactly 11 digits long."

    # Act
    result = is_valid_phone_number(input_data)

    # Assert
    assert result == expected


# scenario 4 - input data isn't a string -> int instead
def test_is_valid_phone_number_unhappy_path_int():
    # Arrange
    input_data = 12345678910
    expected_msg = re.escape("'int' object has no attribute 'isdigit'")

    with pytest.raises(AttributeError, match=expected_msg):
        is_valid_phone_number(input_data)


# scenario 5 - input data isn't a string -> None instead
def test_is_valid_phone_number_unhappy_path_None():
    # Arrange
    input_data = None
    expected_msg = re.escape("'NoneType' object has no attribute 'isdigit'")

    with pytest.raises(AttributeError, match=expected_msg):
        is_valid_phone_number(input_data)
