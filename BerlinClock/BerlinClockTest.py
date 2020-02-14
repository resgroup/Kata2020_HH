import pytest
from .BerlinClock import integer_to_unery_string

def test_unery_yellow_11():
    result = integer_to_unery_string("Y", 11)
    assert result == "YYYYYYYYYYY"

def test_unery_red_7():
    result = integer_to_unery_string("R", 7)
    assert result == "RRRRRRR"    

def test_pad_unery_string():
    result = pad_unery_string('RRR', 7)
    assert result == 'RRROOOO'

def test_pad_unery_string_no_padding():
    result = pad_unery_string('RRRR', 4)
    assert result == 'RRRR'

def test_pad_unery_string_emptry_string():
    result = pad_unery_string('', 3)
    assert result == '000'

def test_pad_unery_string_too_long():
    exception_thrown = false
    try:
        result = pad_unery_string('RRRR', 3)
    except: 
        exception_thrown = True
    assert exception_thrown

def test_create_light_string():
    result = create_light_string("RRRR")
    assert result = "RRRR\n"

def test_hours_to_string():
    result = hours_to_string(16)
    assert result = "RRR0\nR000\n"

def test_minutes_to_string():
    result = minutes_to_string(56)
    assert result = "YYYYYYYYYYY\nYOOO\n"

def test_seconds_to_string_odd():
    result = seconds_to_string(5)
    assert result = 'O'

def test_seconds_to_string_even():
    result = seconds_to_string(8)
    assert result = 'Y'

def test_time_to_string()
    irrelevant_year = 2000
    irrelevant_day = 1
    irrelevant_month = 1
    result = time_to_string(datetime(irrelevant_year,irrelevant_day,irrelevant_month,12,56,1))
    assert result = "O\nRROO\nRROO\nYYYYYYYYYYY\nYOOO\n"


