# importing random library
import random

# choose difficulty
difficulty = input("Enter your game difficult (easy, hard): ")

# guess letter

def letter_guess():
    new_guess = input("Enter your guess (one letter): ")
    # is 1 letter
    if len(new_guess) > 1:
        print("That is too many letters")
        letter_guess()
        
    # check if guess is a letter?
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()
    # checking if letter already guessed
    for letter in all_letters:
        if new_guess not in all_letters:
            print("This isn't a letter")
            letter_guess()
            break
    
    if new_guess in current_guesses:
        print("Letter already guessed")
        letter_guess()
    else:
        current_guesses.append(new_guess)
    return new_guess

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

# find random word - works
def pick_word():
    # open file
    # choose difficulty
    difficulty = input("Enter your game difficult (easy, normal, hard): ")
    with open("words.txt") as file:
        text = file.read()
    # lowercase text
    text = text.lower()
    # replace new lines with spaces
    text = text.replace("\n", " ")

    # put words in list, may need to use \n instead of .split(), pulling words of correct length
    words = []
    if difficulty == "easy":
        for word in text.split(" "):
            if len(word) > 3 and len(word) < 7:
                words.append(word)
    elif difficulty == "normal":
        for word in text.split(" "):
            if len(word) > 5 and len(word) < 9:
                words.append(word)
    else: 
        for word in text.split(" "):
            if len(word) > 7:
                words.append(word)
    # pick random word for game
    target_word = random.choice(words)
    print("The word is ", len(target_word), "letters long.")
    print(target_word)
    return target_word

target_word = pick_word()

# display blanks - works
blanks = (" _ " * len(target_word))
print(blanks)



# already guessed list
past_guess = []


    

    
# from class notes - works
def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter.upper()
    else:
        return "_"



def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) for letter in word]
    print(" ".join(output_letters))


# game has turns - works
def run_game():
    
    display = display_letter(word, current_guesses)
    print(display)
    bad_guesses = 0
    while "_" in display:
        print("Turn: ", bad_guesses + 1)
        new_guess = input("Enter your guess (one letter): ")
        bad_guesses += 1
        if bad_guesses == 8:
            print("Game Over")
            play_again()
            break

# play again? - works
def play_again():
    response = input("Play again? (Y/N): ")
    if response == "Y" or response == "y":
        run_game()
    else:
        print("OK Goodbye! Thanks for playing!")

# random shit - may not be necessary
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