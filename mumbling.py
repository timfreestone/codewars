# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


# capitalise first
# multiply by index number+1
# add a -
def accum(st):
    original_string_length = range(1,len(st))
    new_string = st[0].upper()
    for i in original_string_length:
        new_string = new_string + "-" + st[i].upper() + (st[i]*i).lower()
    return new_string


print(accum("RqaEzty"))


# output = print(accum("cwAt"))
# print(output)
# print("C-Ww-Aaa-Tttt")
# print(output=="C-Ww-Aaa-Tttt")

# type()

