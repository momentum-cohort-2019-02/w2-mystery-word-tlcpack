import random

word = "MAGNITUDE"
current_guesses = ["g", "e", "t"]
def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter.upper() in guesses:
        return letter.upper()
    else:
        return "_"



def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) for letter in word]
    print(" ".join(output_letters))
    return 

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

    # for past in current_guesses:
    if new_guess in current_guesses:
        print("Letter already guessed")
        letter_guess()
    else:
        current_guesses.append(new_guess)
    return new_guess




print_word(word, current_guesses)
letter_guess()
letter_guess()
letter_guess()