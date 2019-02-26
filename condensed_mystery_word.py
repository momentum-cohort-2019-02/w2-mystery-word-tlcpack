import random

def select_difficulty():
    """Asking user to select difficulty of game"""
    difficulty = ''
    while difficulty.lower() not in ['easy', 'normal', 'hard']:
        difficulty = input("WELCOME TO MYSTERY WORD!!\nEnter your game difficult (easy, normal, hard): ")
    return difficulty

def determine_word_list(difficulty):
    """Determining random-word length based on difficulty input"""
    with open("words.txt") as file:
        text = file.read()
        file.close
    text = text.lower()
    text = text.replace("\n", " ")
    words_list = []
    if difficulty == "easy":
        for word in text.split(" "):
            if len(word) > 3 and len(word) < 7:
                words_list.append(word)
    if difficulty == "normal":
        for word in text.split(" "):
            if len(word) > 5 and len(word) < 9:
                words_list.append(word)
    if difficulty == "hard":
        for word in text.split(" "):
            if len(word) > 7 :
                words_list.append(word)

    return words_list

def get_final_target_word():
    """Picking word from list for user to guess"""
    filtered_list = determine_word_list(select_difficulty())
    target_word = random.choice(filtered_list)
    print("The word is ", len(target_word), "letters long.")
    return target_word

def is_letter_input_valid(user_input):
    """Is input 1 character long, a letter, and not previously guessed"""
    return len(user_input) == 1 and user_input.isalpha() and user_input not in  current_guesses

def get_letter_input():
    """Getting the letter guess from the user"""
    new_guess = input("Enter your guess (one letter): ").casefold()
    while not is_letter_input_valid(new_guess):
        print("Invalid response. Please try again")
        new_guess = input("Enter your guess (one letter): ").casefold()
    return new_guess


def showing_guessed_letters(word, display_letters):
    """Display blanks and guessed letters of target word"""
    show_letters = []
    for letter in word.casefold():
        if letter in display_letters:
            show_letters.append(letter.upper())
        else:
            show_letters.append("_")
    return " ".join(show_letters)

def play_again():
    """Asks user if they would like to replay game"""
    response = input("Play again? (Y/N): ")
    if response.lower() == "y" or response == "yes":
        run_game()
    else:
        print("OK Goodbye! Thanks for playing!")
        return

current_guesses = []
def print_opening_display():
    current_display = showing_guessed_letters(get_final_target_word(), current_guesses)
    print(current_display)

print_opening_display()