# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


# detect a word (space?)
# index into it
# add the hardcoded string


def pig_it(text):
    words = text.split(" ")
    pig_latin_list = []
    pig_latin_string = ""
    for word in words:
        if word.isalpha():
            word = word[1:] + word[0] + "ay"
        pig_latin_list.append(word)
    for word in pig_latin_list:
        pig_latin_string = pig_latin_string + word + " "
    return pig_latin_string.strip()



pig_it('Pig latin is cool') # igPay atinlay siay oolcay