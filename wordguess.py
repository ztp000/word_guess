import random
import os

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the word_list.txt file
file_path = os.path.join(current_dir, "word_list.txt")

# Open the file using the absolute path
with open(file_path, "r") as file:
    lines = file.readlines()

def pick_random_word(list):
    word = [line.strip() for line in list]
    random_word = random.choice(word).lower()
    return random_word

def game():

    def debug():
        print("_____debug_____")
        print("Word: " + random_word)
        print("Stripped word: " + strip_random_word(random_word))
        print("Guessed_letters: ")
        print(guessed_letters)
        print("_____debug_____")

    def display(word):
        screen = ""
        for letter in random_word:
            if letter in guessed_letters:
                screen += letter
            if letter not in guessed_letters:
                screen += " * "
        print(screen)

    def check_the_guess(letter):
        if letter not in guessed_letters and isinstance(letter, str) and len(letter) == 1 and letter in random_word:
            guessed_letters.append(letter)
            return True
        elif letter not in random_word:
            print("Wrong.")
            return False

    def strip_random_word(word):
        stripped_string = ""
        for letter in word:
            if letter not in stripped_string:
                stripped_string += letter
        return stripped_string

    lives = 5
    random_word = pick_random_word(lines)
    guessed_letters = []

    while sorted("".join(guessed_letters)) != sorted(strip_random_word(random_word)):
        debug()
        print("------")
        display(random_word)
        print("------")
        print(f"You have {lives} guess left.")
        guess = input("Your Guess: ").lower()
        check_the_guess(guess)
        if check_the_guess(guess) == False:
            lives -= 1
        if lives < 1:
            break
    guessed_letters.clear()

    if lives > 0:
        print("You Win")
    if lives < 1:
        print("You Lost")

while True:
    game()
    input("New Game?")