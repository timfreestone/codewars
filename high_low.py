# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5") # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    new_list = []
    for number in numbers.split(" "):
        new_list.append(int(number))
    return f"{sorted(new_list)[-1]} {sorted(new_list)[0]}"

   
 

print(high_and_low(("7 12 -7 16 99 100 2 3 8 87")))






    # numbers = list(numbers.replace(" ", ","))
#    numbers = [x for x in numbers if x not in [","]]
#     print(numbers)
#     return numbers[-1], numbers[0]


#  for i in numbers:
#         if i.isdigit():
#             new_list.append(i)
    
#     print(new_list)
#     return new_list
