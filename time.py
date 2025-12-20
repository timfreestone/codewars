# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.
import math

def make_readable(seconds):
    hours = math.floor(seconds / 60 / 60)
    minutes = math.floor(seconds / 60 ) - hours * 60
    seconds = seconds - minutes * 60 - hours * 60 * 60

    if len(str(hours)) == 1:
        hours = f"0{hours}"
    else:
        hours = f"{hours}"

    if len(str(minutes)) == 1:
        minutes = f"0{minutes}"
    else:

        minutes = f"{minutes}"
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"

    return f"{hours}:{minutes}:{seconds}"
