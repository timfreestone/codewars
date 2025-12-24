import string

def rot13(message):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    new_message = ""
    for letter in message:
        if letter in alphabet_lower:
            letter_index = alphabet_lower.index(letter)
            replacement = replace(letter, alphabet_lower[letter_index+3])
            new_message = new_message + replacement
        elif letter in alphabet_upper:
            letter_index = alphabet_upper.index(letter)
            replacement = replace(letter, alphabet_upper[letter_index+3])
            new_message = new_message + replacement
        else:
            new_message = new_message + replacement
    return new_message


# replace function with a loop?
# index over a list
# deal with cases (use if x in a, then do this, elif in b, do this, else do ntohing)


print(rot13("Hello World5!"))
