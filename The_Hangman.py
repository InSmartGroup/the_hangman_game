import random
import sys
from the_hangman_dictionary import THE_HANGMAN_DICTIONARY as HD
from the_hangman_art import THE_HANGMAN_ART as HA
from the_hangman_art import THE_HANGMAN_LOGO as HL
from time import sleep


def letter_swap():
    while guess in random_word:
        letter_position = random_word.index(guess)
        random_word[letter_position] = '-'
        secret_word[letter_position] = guess


def intro():
    print(HL)
    sleep(2)
    print("WELCOME TO 'THE HANGMAN'.")
    print(f"I've guessed the word that has {random_word_length} letters.")
    print(f"You have {lives} guess attempts to guess the word.")
    print("Good luck!")
    sleep(3)


lives = 6
random_word = list(random.choice(HD))
display_word = random_word.copy()
random_word_length = len(random_word)
if random_word_length >= 9:
    lives = 8

mistakes_count = 0
used_letters = []
secret_word = []
for letter in range(random_word_length):
    secret_word.append('_')

intro()

while True:
    print()
    print(f"Word to guess: {''.join(secret_word)}")
    print(f"Letters you've tried: {', '.join(used_letters)}")
    guess = input("Make your guess: ").lower()

    if guess == 'quit' or guess == 'exit' or guess == 'stop':
        print("Terminating the game", file=sys.stderr)
        sys.exit()

    if guess.isdigit():
        print()
        print("Please use letters to play the game.", file=sys.stderr)
        continue

    elif len(guess) > 1:
        print()
        print("Please use single letters to play the game.", file=sys.stderr)
        continue

    letter_swap()

    if guess in used_letters:
        print()
        print(f"You already guessed '{guess}'.\nTry another letter.", file=sys.stderr)
        continue

    if '_' not in secret_word:
        print()
        print(f"You made it!\nThe word is '{''.join(display_word)}'.\nCongratulations!", file=sys.stderr)
        print()
        print("Would you like to play again? Type 'yes' or 'no'.")
        play_again = input().lower()
        if play_again == 'yes' or play_again == 'y' or play_again == 'sure' or play_again == 'go':
            random_word = list(random.choice(HD))
            random_word_length = len(random_word)
            lives = 6
            if random_word_length >= 10:
                lives = 8
            mistakes_count = 0
            used_letters = []
            secret_word = []
            for letter in range(random_word_length):
                secret_word.append('_')
            intro()
            continue
        elif play_again == 'n' or play_again == 'no' or play_again == 'quit' or play_again == 'nope':
            print("Thank you for playing!")
            sys.exit()

    if lives == 0:
        print()
        print(f"You ran out of lives.\nThe word was '{''.join(display_word)}'.\nGame Over.", file=sys.stderr)
        print()
        print("Would you like to play again? Type 'yes' or 'no'.")
        play_again = input().lower()
        if play_again == 'yes' or play_again == 'y' or play_again == 'sure' or play_again == 'go':
            random_word = list(random.choice(HD))
            random_word_length = len(random_word)
            lives = 6
            if random_word_length >= 10:
                lives = 8
            mistakes_count = 0
            used_letters = []
            secret_word = []
            for letter in range(random_word_length):
                secret_word.append('_')
            intro()
            continue
        elif play_again == 'n' or play_again == 'no' or play_again == 'quit' or play_again == 'nope':
            print("Thank you for playing!")
            sys.exit()

    if guess in secret_word:
        print(HA[mistakes_count])
        if guess not in used_letters:
            used_letters.append(guess)
        continue

    if guess not in random_word:
        if guess not in used_letters:
            used_letters.append(guess)
        mistakes_count += 1
        lives -= 1
        print(HA[mistakes_count])
        print(f"Oops! No '{guess}' in this word.", file=sys.stderr)
        continue
