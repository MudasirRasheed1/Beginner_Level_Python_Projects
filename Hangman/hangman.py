from data import gen_word

def play_hangman():
    choice = 'y'    
    while choice == 'y' or choice == 'Y':
        random_word = gen_word()
        print("\n\nWelcome to Hangman")
        name = input("whats your name?  ")
        print(f"Hello {name}! Lets play Hangman!")
        print("I have chosen a word it is related to programming and technologies, you have to guess it letter by letter")
        print("The word contains ", len(random_word), "letters\n")

        tries = 10
        user_gussed_characters = " "
        while tries > 0:
            
            blank = len(random_word)
            for character in random_word:
                if character in user_gussed_characters:
                    print(character, end=" ")
                    blank -= 1
                else:
                    print("_", end=" ")

            print()
            if blank == 0:
                print("\nCongratulations!!! , You guessed the word!")
                print("You survived!")
                break
            character = input("\nGuess a letter: ")
            
            if character in user_gussed_characters:
                print("\nyou have already entered this character")
                continue
            
            elif character in random_word:
                user_gussed_characters += character
                continue
            else:
                user_gussed_characters += character
                tries -= 1
                print("\nThat letter doesn't appear in the word")
                print(f"You have {tries} tries left")
            if tries == 0:
                print("\nYou lost!")
                print(" The word was", random_word)
                print("Better luck next time!")
        choice = input("\n\nEnter y to play again or n to exit:  ")
        
if __name__ == "__main__":
    play_hangman()
        