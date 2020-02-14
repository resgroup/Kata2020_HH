def integer_to_unery_string(digit_character, integer_value):
    return digit_character*integer_value

def pad_unery_string(string, padded_length)
    padding_length = padded_length - len(string)
    if padding_length < 0:
        Exception
    return string + "0" * padding_length 

def create_light_string(string):
    string + "\n"

def hours_to_string(hours):
    return create_light_string(pad_unery_string(integer_to_unery_string(hours/5, 'R'), 4)) +\
           create_light_string(pad_unery_string(integer_to_unery_string(hours%5, 'R'), 4))

def minutes_to_string(minutes):
    return create_light_string(pad_unery_string(integer_to_unery_string(minutes/5, 'Y'), 11)) +\
           create_light_string(pad_unery_string(integer_to_unery_string(minutes%5, 'Y'), 4))

def seconds_to_string(seconds):
    return create_light_string(pad_unery_string(integer_to_unery_string(seconds%2, 'Y'), 1))
