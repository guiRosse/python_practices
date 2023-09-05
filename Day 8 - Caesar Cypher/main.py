import cls
from logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
go_again = "y"

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(start_text, shift_position, direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            if direction == "encode":
                letter_position = alphabet.index(letter) + shift_position
                if letter_position >= len(alphabet):
                    letter_position = letter_position - len(alphabet)
                encrypted_letter = alphabet[letter_position]
                # print(encrypted_letter)
                end_text += encrypted_letter
            elif direction == "decode":
                letter_position = alphabet.index(letter) - shift_position
                if letter_position >= len(alphabet):
                    letter_position = letter_position - len(alphabet)
                decrypted_letter = alphabet[letter_position]
                # print(decrypted_letter)
                end_text += decrypted_letter
        else:
            end_text += letter
    print(f"The {direction}d word is {end_text}")

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


while go_again.lower() == "yes" or go_again.lower() == "y":
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    cls.clear_screen()
    print(logo)
    print("***************************\n")
    # print("Test Runs")
    # caesar("civilization", 5, "encode")
    # caesar("hnanqnefynts", 5, "decode")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift_position=shift, direction=direction)
    
    go_again = input("Would you like to go again? Typye 'Yes' or 'No' : ")