#Step 1 
import random
import cls #    Import a small fn for clearing screen conveniently

word_list = ["aardvark", "baboon", "camel"]
blanks = [] #   A placeholder for my blanks for the next steps
mystery_word = ""   #   Only used to displaay the list items of [blanks] as an actual word
player_status = "Your word is "

cls.clear_screen()

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print("*******************************************************************\n\n")

print(f"**TEST MODE ON*** \nThe selected word from the list is {chosen_word}")  # Enabled for testing only. Showing the selected word.

for letter in chosen_word:
    mystery_word += "_"

print(player_status, mystery_word)

print("\n\n*******************************************************************")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("\n\nChoose a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
mystery_word = ""
for letter in chosen_word:
    if guess == letter:
        blanks.append(letter)   # Blanks list item get to be replaced by the uderscore
        # print(1)
    else:
        blanks.append("_")

for item in blanks:
    mystery_word += item
print(mystery_word)