#I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.
#Can you figure out what's wrong here?

def swap_values(args):
    original_0 = args[0]
    original_1 = args[1]
    args[0] = original_1
    args[1] = original_0

