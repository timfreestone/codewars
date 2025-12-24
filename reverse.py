# Write a function that takes in a string of one or more words, and returns the same string, 
# but with all words that have five or more letters reversed (just like the name of this kata). 
# Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    word_list = sentence.split(" ")
    reversed_list = []
    for word in word_list:
        if len(word) >= 5:
            reversed_list.append(word[::-1])
        else:
            reversed_list.append(word)
    reversed_string = ""
    for word in reversed_list:
        reversed_string = reversed_string + word + " "
    return reversed_string.strip()


print(spin_words("Hey fellow warriors"))

# split on the space
# put into list
# if len, reverse, else don't
# add to the string sentence
# plus a space?