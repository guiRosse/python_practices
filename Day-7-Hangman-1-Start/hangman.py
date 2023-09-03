#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]
blanks = [] #   A placeholder for my blanks for the next steps
mystery_word = ""

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

print(f"The chosen word is {chosen_word}")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("\n\nChoose a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

for letter in chosen_word:
    blanks.append("_")

for blank in blanks:
    mystery_word+= blank

for letter in chosen_word:
    if guess == letter:
        blanks.append(letter)   # Blanks list item get to be replaced by the uderscore
        # print(1)
    else:
        print(0)

print(mystery_word)