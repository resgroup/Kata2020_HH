import pytest
import str2bool
def test_str2bool():
    output_value = str2bool('y')
    expected_output_value = True

    assert type(expected_output_value) == type(output_value)

if __name__ == '__main__':
    test_str2bool()