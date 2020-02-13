import pytest
from utilities.str2bool import str2bool

def test_str2bool():
    output_value = type(str2bool('y'))
    expected_output_value = bool

    assert expected_value == actual_value

if __name__ == '__main__':
    test_str2bool()