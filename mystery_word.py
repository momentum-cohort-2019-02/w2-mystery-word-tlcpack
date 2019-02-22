# importing random library
import random

# choose difficulty
difficulty = input("Enter your game difficult (easy, hard): ")

# guess letter
new_guess = input("Enter your guess (one letter): ")



def pick_word_easy():
    # open file
    with open("words.txt") as file:
        text = file.read()
    # lowercase text
    text = text.lower()
    # replace new lines with spaces
    text = text.replace("\n", " ")

    # put words in list, may need to use \n instead of .split(), pulling words of correct length
    words = []
    for word in text.split(" "):
        if len(word) > 3 and len(word) < 7:
            words.append(word)

    # pick random word for game
    target = random.choice(words)
    print(target)
    return target

target = pick_word_easy()

# display blanks
print(" _ " * len(target))

# how many blanks
print("The word is ", len(target), "letters long.")

# already guessed list
past_guess = []

# loop for turns
for turn in range(8):
    print("Turn", turn + 1)
    new_guess = input("Enter your guess (one letter): ")
    # already guessed list
    past_guess = []
    # checking if letter already guessed
    for past in past_guess:
        if past == new_guess:
            print("Letter already guessed")
        else:
            past_guess.append(new_guess)
    
# from class notes
def display_letter(letter, guesses):
    """
    Conditionally display a letter. If the letter is already in
    the list `guesses`, then return it. Otherwise, return "_".
    """
    if letter in guesses:
        return letter
    else:
        return "_"

[display_letter(letter, current_guesses) for letter in word]

def print_word(word, guesses):
    output_letters = [display_letter(letter, guesses) for letter in word]
    print(" ".join(output_letters))
    
print_word(word, guesses)
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