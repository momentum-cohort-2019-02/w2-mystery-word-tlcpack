import random

def select_difficulty():
    """Asking user to select difficulty of game"""
    difficulty = None
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

filtered_list = determine_word_list(select_difficulty())
target_word = random.choice(filtered_list)
print("The word is ", len(target_word), "letters long.")
current_guesses = []

def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter.upper()
    else:
        return "_"

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


