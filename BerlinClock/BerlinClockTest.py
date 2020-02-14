import pytest
from .BerlinClock import integer_to_unery_string

def test_unery_yellow_11():
    result = integer_to_unery_string("Y", 11)
    assert result == "YYYYYYYYYYY"

def test_unery_red_7():
    result = integer_to_unery_string("R", 7)
    assert result == "RRRRRRR"    
