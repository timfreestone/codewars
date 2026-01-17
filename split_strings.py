# Complete the solution so that it splits the string into strings of two characters in a list/array (depending on the language you use). 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:

# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
    result = []
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        if len(pair) == 1:
            pair += "_"
        result.append(pair)
    return result

print(solution('abcdefv'))