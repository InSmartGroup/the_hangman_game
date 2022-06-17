with open('the_hangman_dictionary.txt') as in_file:
    out_file = in_file.read().strip().split("\n")

THE_HANGMAN_DICTIONARY = [x.lower() for x in out_file]
