# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If a number is a multiple of both 3 and 5, only count it once.


# no double counting
# modulo of 3 or 5 equal to 0
# less than the input
# add them all up
# no negative numbers
# loop over every number in between to check if multiple?

def solution(number):
    sum = 0
    for numeral in range (1,number):
        if number < 0:
            return 0
        elif numeral % 3 == 0:
            sum = sum + numeral
        elif numeral % 5 == 0:
            sum = sum + numeral
    return sum
