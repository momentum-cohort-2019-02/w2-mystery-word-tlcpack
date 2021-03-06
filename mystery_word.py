# importing random library
import random

current_guesses = []

def pick_word():
    """Asking user for difficulty, creating word list based on response"""
    # open file
    # choose difficulty
    
    with open("words.txt") as file:
        text = file.read()
        file.close

    # # # does with auto-close file?
    # lowercase text
    text = text.lower()

    # replace new lines with spaces
    text = text.replace("\n", " ")
   

    # put words in list, may need to use \n instead of .split(), pulling words of correct length
    words = []
    pick = True

    # picking letter choice loop
    while pick:
        difficulty = input("WELCOME TO MYSTERY WORD!!\nEnter your game difficult (easy, normal, hard): ")
        difficulty = difficulty.lower()
        if difficulty == "easy":
            for word in text.split(" "):
                if len(word) > 3 and len(word) < 7:
                    words.append(word)
            pick = False
        elif difficulty == "normal":
            for word in text.split(" "):
                if len(word) > 5 and len(word) < 9:
                    words.append(word)
            pick = False
        elif difficulty == "hard":
            for word in text.split(" "):
                if len(word) > 7 :
                    words.append(word)
            pick = False
        
        # make response for invalid response
        else: 
            print("Invalid response")
            
    
    # pick random word for game
    target_word = random.choice(words)
    print("The word is ", len(target_word), "letters long.")
    
    print(target_word) # for testing
    return target_word

# final_target_word = pick_word()
# find unique letters in final word

# for letter in final_target_word:
#     if letter in all_letters and letter not in unique_letters_in_final:
#         unique_letters_in_final.append(letter)

# this was needed earlier, no longer
# all_letters = "abcdefghijklmnopqrstuvwxyz"
# unique_letters_in_final = []

def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter.upper()
    else:
        return "_"


# def print_word(word, guesses):
#     output_letters = [display_letter(letter, guesses) for letter in final_target_word]
#     print(" ".join(output_letters))
#     return



def letter_guess():
    """Asks user for letter, validates guess, returns if valid"""
    
    # check if guess is a letter
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    # checking if entry is valid already guessed
    
    while True:
        new_guess = input("Enter your guess (one letter): ")
        new_guess = new_guess.lower()
        if new_guess in current_guesses:
            print("\nLetter already guessed\n")
            
        elif len(new_guess) != 1:
            print("\nI need one letter\n")
            
        elif new_guess not in all_letters:
            print("\nThis isn't a letter\n")    
            
        else:
            current_guesses.append(new_guess)
            return new_guess


def run_game():
    """The game"""
    
    # clears guesses from previous game
    del current_guesses[:]
    final_target_word = pick_word()
    
    # display initial blanks
    print("_ " * len(final_target_word))
    
    # find unique letters in final word
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    unique_letters_in_final = []
    for letter in final_target_word:
        if letter in all_letters and letter not in unique_letters_in_final:
            unique_letters_in_final.append(letter)
    
    # displays blanks with guessed letters once game begins
    def print_word(word, guesses):
        output_letters = [display_letter(letter, guesses) for letter in final_target_word]
        print(" ".join(output_letters))
        return

    # print(unique_letters_in_final) # for testing
    # print("# unique letter", len(unique_letters_in_final)) # for testing
    bad_guesses = 0
    winner_check = []

    # can also use for loop to compare guessed letters to word letters
    # for guess in current_guesses:
    while True:
        
        #showing turn
        print("Turn: ", bad_guesses + 1)
        
        # showing current guesses # for testing
        print("Your current guesses: ", ''.join(current_guesses))
        # print(winner_check) 

        #running guess letter fxn
        recent = letter_guess()
        
        #printint target word as a check
        print_word(final_target_word, current_guesses)

        # declaring winner
        # adding correctly guessed letter to a good guess list
        for letter in final_target_word:
            if letter in current_guesses and letter not in winner_check:
                winner_check.append(letter)
        # comparing len of unique letter lists between word and good guesses
        if len(unique_letters_in_final) == len(winner_check):
            print("\nYou win!\n")
            play_again()
            return  
        
        if recent in final_target_word:
            print("\nGood guess!\n")
    
        else:
            print("\nNot quite\n")
            bad_guesses += 1
        
        #ending game with too many guesses
        if bad_guesses == 8:
            print(f"Game Over. The word is {final_target_word}.")
            play_again()
            break


def play_again():
    """Asks user if they would like to replay game"""
    response = input("Play again? (Y/N): ")
    if response.lower() == "y" or response == "yes":
        run_game()
    else:
        print("OK Goodbye! Thanks for playing!")
        return

run_game()

# random shit - may not be necessary - maybe for running text file
# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)

# testing letter_guess
# past_guess = []
# def letter_guess():
#     new_guess = input("Enter your guess (one letter): ")
#     # is 1 letter
#     if len(new_guess) > 1:
#         print("That is too many letters")
#         letter_guess()
        
#     # already guessed list
#     # past_guess = []
#     # check if guess is a letter?
#     all_letters = "abcdefghijklmnopqrstuvwxyz"
#     all_letters += all_letters.upper()
#     # checking if letter already guessed
#     for letter in all_letters:
#         if new_guess not in all_letters:
#             print("This isn't a letter")
#             letter_guess()
#             break
#     for past in past_guess:
#         if new_guess in past_guess:
#             print("Letter already guessed")
#             letter_guess()
            
#         else:
#             past_guess.append(new_guess)
#             return new_guess

# word = 
# guesses = []
# for letter in word:
#     if letter not in guesses:
#         win = False
# all function can help with this
# all([letter in guesses for letter in word])

# if difficulty in ['easy', 'medium', 'hard']: