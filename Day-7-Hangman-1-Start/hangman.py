#Step 1 
import random
import cls #    Import a small fn for clearing screen conveniently

word_list = ["aardvark", "baboon", "camel"]
blanks = []         #   A placeholder for my blanks for the next steps
mystery_word = ""   #   Only used to displaay the list items of [blanks] as an actual word

cls.clear_screen()

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print("*******************************************************************\n\n")

print(f"**TEST MODE ON*** \nThe selected word from the list is {chosen_word}\n\n")  # Enabled for testing only. Showing the selected word.

for _ in chosen_word:
    blanks.append("_")
    mystery_word += "_"

print(f"Your word is {mystery_word}")

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all 
# the letters in the chosen_word and 'display' has no more 
# blanks ("_"). Then you can tell the user they've won.

has_won = False # Variable for letting the game go on

print("\n\n*******************************************************************")

while not has_won:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("\n\nChoose a letter: ").lower()
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    #TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
    for index, letter in enumerate(chosen_word):
        if guess == letter:
            # print(index)
            # print(letter)
            blanks[index] = letter   # Blanks list item get to be replaced by the guessed letter
            
    print(blanks)

    if "_" not in blanks:
        has_won = True
        print("You have won")