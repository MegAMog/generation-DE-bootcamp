#Test utils/ utils.is_valid_price function
from utils.utils import is_valid_price 
import re, pytest


# scenario 1 - input data is a positive float
def test_is_valid_price_happy_path_positive_float():
    # Arrange
    input_data = 1.0
    expected = True, ""

    # Act
    result = is_valid_price(input_data)

    # Assert
    assert result == expected


# scenario 2 - input data is an int
def test_is_valid_price_happy_path_positive_int():
    # Arrange
    input_data = 1
    expected = True, ""

    # Act
    result = is_valid_price(input_data)

    # Assert
    assert result == expected


# scenario 3 - input data is a negative float
def test_is_valid_price_happy_path_negative_float():
    # Arrange
    input_data = -1.0
    expected = False, "Price cannot be negative."

    # Act
    result = is_valid_price(input_data)

    # Assert
    assert result == expected


# scenario 4 - input data is a negative float
def test_is_valid_price_happy_path_str():
    # Arrange
    input_data = 'one'
    expected = False, "Price must be a valid number (should contain only digits)."

    # Act
    result = is_valid_price(input_data)

    # Assert
    assert result == expected


# scenario 5 - input data isn't a string -> int instead
def test_is_valid_price_unhappy_path_int():
    # Arrange
    input_data = None
    expected_msg = re.escape("float() argument must be a string or a real number, not 'NoneType'")

    with pytest.raises(TypeError, match=expected_msg):
        is_valid_price(input_data)
