# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, "r")
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    return all([True if l in letters_guessed else False for l in secret_word])


def get_guessed_word(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    guess = ["_" for _ in range(len(secret_word))]

    for i, letter in enumerate(secret_word):
        if letter in letters_guessed:
            guess[i] = letter

    return " ".join(guess)


def get_available_letters(letters_guessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    return "".join(
        [letter for letter in string.ascii_lowercase if letter not in letters_guessed]
    )


def hangman(secret_word):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    print("	Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    mistakes_made = 0
    letters_guessed = []
    while mistakes_made < 8:
        print("-" * 11)
        print(f"You have {8 - mistakes_made} guesses left")
        print(f"Available Letters: {get_available_letters(letters_guessed)}")
        l_guessed = input("Please guess a letter: ").lower()

        if l_guessed in letters_guessed:
            print(
                f"Oops! You've already guessed that letter: {get_guessed_word(secret_word, letters_guessed)}"
            )
        elif l_guessed not in secret_word:
            letters_guessed.append(l_guessed)
            print(
                f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}"
            )
            mistakes_made += 1
        else:
            letters_guessed.append(l_guessed)
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

        if is_word_guessed(secret_word, letters_guessed):
            print(f"Congratulations, you won! {secret_word}")
            break

    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secret_word while you're testing)

secret_word = choose_word(wordlist).lower()
hangman(secret_word)
