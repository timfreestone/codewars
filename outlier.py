# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)


# not correct yet, but getting there I think
def find_outlier(integers):
    if (integers[0] % 2 + integers[1] % 2 + integers[2] % 2) in (0,1):
        outlier_type = "Odd"
    else:
        outlier_type = "Even"
    print(outlier_type)
    for integer in integers:
        if outlier_type == "Even" and integer % 2 == 0:
            return integer
        elif outlier_type =="Odd" and integer % 2 != 0:
            return integer





