#Write a function that checks if a given string (case insensitive) is a palindrome.
# A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.


def is_palindrome(s):
    reverse_s = ""
    i = 0
    original_string = s
    original_length = len(s)
    while i < original_length:
        reverse_s = reverse_s + s[-1]
        s = s[:-1]
        i = i + 1 
    if original_string.lower() == reverse_s.lower():
        return True
    else:
        return False

    

print(is_palindrome("Happy"))
    