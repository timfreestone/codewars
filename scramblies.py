# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# Notes:

# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


# inefficient solution
def scramble(s1, s2):
    for i in s2:
        if i not in s1:
            return False
        idx = s1.index(i)
        s1 = s1[:idx] + s1[idx+1:]
    return True

# efficient solution

def scramble(s1, s2):
    counts = {}
    for ch in s1:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in s2:
        if counts.get(ch, 0) == 0:
            return False
        counts[ch] -= 1

    return True



print(scramble('katas', 'steak'))