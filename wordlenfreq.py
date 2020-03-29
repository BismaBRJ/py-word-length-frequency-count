# Word Length Frequency Counter
# by Bisma Joyosumarto
# made on a Sunday evening, 29 March 2020

# visual 80 character limit
# .......1.........2.........3.........4.........5.........6.........7.........8
# 345678901234567890123456789012345678901234567890123456789012345678901234567890

# Introduction
print("Welcome to Word Length Frequency Counter.")
print("This program accepts a string, then seperates out each \"word\",")
print("in which \"word\"s are considered to be separated by spaces.")
print("After that, the length of each \"word\" is counted, like tallying.")
print("At the end, the result of tallying will be shown:")
print("- how many words are 1 character in length,")
print("- how many words are 2 characters in length,")
print("- how many words are 3 characters in length,")
print("and so on.")
print("If no words of a particular character length are found,")
print("then it won't be displayed.")
print()

# Entering the string
print("Please enter your string: ")
the_document = input()
print()
print("String accepted!")
print()
print("Just to confirm, your string was:")
print(the_document)
print()
print("Right? Okay. Counting...")
print()

# COUNTING STEP 1: separate into words
word_list = the_document.split()
# this is a method of the String class,
# which "converts" it into a list of "word"s,
# assuming that "word"s are separated by spaces.

# COUNTING STEP 2: make a Python dictionary,
# where key:value pairs will represent length:amount.

# Here's what I mean, let's say we have a string "aye aye captain yeah"
# If so, the dict is gonna be as follows: {3:2, 4:1, 7:1}
# which means, of length 3 characters, we found 2 words,
# of length 4 characters, we found 1 word,
# and of length 7 characters, we found 1 word.

# Okay let's do this.
length_amount_dict = {}

# COUNTING STEP 3: iterate over each word

for current_word in word_list:
    # Obtain length of current word
    current_length = len(current_word)

    # Check if the current length already exists as a key
    try:
        # We check by trying to obtain the value of the key,
        # assuming that the key exists
        random_assingment = length_amount_dict[current_length]
    except KeyError:
        # If the key doesn't exist, the KeyError exception is raised.
        # this means that a word of length current_length,
        # has never been found before! This is our *first* discovery.
        # assign the first tally to it!
        length_amount_dict[current_length] = 1
    else:
        # But if it does exist already... let's just add to it.
        length_amount_dict[current_length] += 1
        # note the use of the += operator, which adds to what already exists.

    # Then, the for loop checks the next word. And so on, until it's done.

# COUNTING STEP 4: sorting the keys
# Now, the thing is, the keys are probably messed up.
# Using the "aye aye captain yeah" example,
# it would still be {3:2, 7:1, 4:1}
# but we want the length keys to be in ascending order, like {3:2, 4:1, 7:1}.

# To do that, first of all, let's just get a list of all the keys.
list_of_keys = list(length_amount_dict)
# and then sort it:
list_of_keys.sort()
# Alright, great! That's an ascending list of our keys.

# Now let's make another dictionary...
sorted_dict = {}
# ... which will use the sorted list of keys,
# to obtain each value from the original dictionary, in a sorted manner.

for current_key in list_of_keys:
    sorted_dict[current_key] = length_amount_dict[current_key]

# This is basically just copying the contents of the dictionary into a new one,
# but we're copying it in order: starting from the smallest key value.

# RESULTS
# Alright, now we just need to tell the user our results.
print("Counting done! Here are the results:")
# Let's iterate!
for current_key in list_of_keys:
    if sorted_dict[current_key] == 1:
        # If there is only one word,
        print("- Of character length " + str(current_key) +
              ", we counted 1 word.")
    else:
        # But if there is more than one word,
        print("- Of character length " + str(current_key) + ", we counted " +
              str(sorted_dict[current_key]) + " words.")
print()
print("Thank you!")
