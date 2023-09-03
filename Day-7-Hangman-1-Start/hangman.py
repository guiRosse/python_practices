#Step 1 
import random
import cls #    Import a small fn for clearing screen conveniently


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
stage_num = len(stages)-1
word_list = ["aardvark", "baboon", "camel"]
blanks = []         #   A placeholder for my blanks for the next steps
mystery_word = ""   #   Only used to displaay the list items of [blanks] as an actual word
has_won = False # Variable for letting the game go on with winning chances
has_lost = False # Variable for letting the game go on as losing

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

print("\n\n*******************************************************************")

while not has_won and not has_lost:
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("\n\nChoose a letter: ").lower()
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

    #TODO-3.1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                # print(index)
                # print(letter)
                blanks[index] = letter   # Blanks list item get to be replaced by the guessed letter
        

    elif stage_num == 0:
        has_lost = True
        print(stages[stage_num])
        print("Game over! You lose")
    else:
        print(stages[stage_num])
        stage_num-=1
    
    print(f"{' '.join(blanks)}")

    if "_" not in blanks:
        has_won = True
        print("You have won")