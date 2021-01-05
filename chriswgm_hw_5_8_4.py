"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/10/2020
Homework Problem: #5.8.4
Description: A program that take user input for a file name, gets the words
in the file and prints the words with once occurrence

"""

# Importing convenience methods from libraries
from os import path
from string import punctuation
from collections import Counter


class WordLengthError(Exception):
    """
    A Class inheriting for `Exception` for common error that is not built-in
    """
    pass


ALLOWED_PUNCTUATIONS = ["'", "-"]
PUNCTUATIONS = [p for p in punctuation if p not in ALLOWED_PUNCTUATIONS]


def validate_file_existence(file_name):
    """
    Checks if the file exist

    :param file_name: A string representing a file name
    """
    if not (path.isfile(file_name)):
        raise FileNotFoundError("There was no file found for the given name. "
                                "Please try again...")


def validate_words_infile(words_param):
    """
    Includes validation for words that are longer than the longest word found in
    an english dictionary. Just for fun and practice as some of this code will
    be reused for my final project...

    "Pneumonoultramicroscopicsilicovolcanoconiosis" (45 Letters)

    :param words_param: A list of strings for evaluation

    """
    if len(words_param) <= 0:
        raise ValueError("No words found in file. Please update your file and "
                         "try again...")

    if len([w for w in words_param if len(w) > 45]) > 0:
        raise WordLengthError("Hmmm... Something here looks suspicious! "
                              "We found some words that are too long. "
                              "Are you trying to fool proof me? "
                              "Please try again...")


def list_words_once_occurrence(words_param):
    """
    Gets the words with one occurrence

    :param words_param: A list of strings for evaluation
    :return: A list of string with one occurrence
    """

    # Using `Counter` for convenience extraction of most common words
    common_words_list = Counter(words_param).most_common()

    # Gets the count of the less common word in list, which is 1
    _, min_c = min(common_words_list)

    # Validates that there is words with occurrence once
    if min_c > 1:
        raise WordLengthError("No word with one occurrence found. "
                              "Please update your file and try again...")

    # Gets the words with occurrence once
    words_once = [str(w[0]) for w in list(filter(lambda x: x[1] is min_c,
                                                 common_words_list))]

    return words_once


def get_words_from_file(file_name):
    """
    Gets the list of words in the file from the given file name

    :param file_name: A string representing a file name
    :return: A list of words for evaluation
    """

    # Opens the file with a given name or raise exception
    try:
        words_file = open(file_name, "r")
    except Exception as d:
        print(f"{d.__class__.__name__}: {d}")
        return None

    # Reads the file after opening or raise exception
    try:
        words = words_file.read()
    except Exception as f:
        print(f"{f.__class__.__name__}: {f}")
        return None
    finally:
        words_file.close()

    # Removes punctuations from words
    words = "".join([w if w not in PUNCTUATIONS else " " for w in words])

    # Super comprehensive list at a quadruple level looping
    words = ["".join([w4 if w4 not in PUNCTUATIONS else "" for w4 in w3])
             for w3 in [w2 for w1 in words.splitlines() for w2 in w1.split()]]

    return words


if __name__ == '__main__':

    # Loop to recollect user input if program founds error
    while True:

        # Gets file name to read from the user via input
        words_file_name = input("Please enter your file's name including the "
                                "file's extension if any:")

        try:
            validate_file_existence(words_file_name)
        except FileNotFoundError as a:
            print(f"{a.__class__.__name__}: {str(a.args[0])}")
            continue
        else:
            words_main = get_words_from_file(words_file_name)

        try:
            validate_words_infile(words_main)
            words_main = list_words_once_occurrence(words_main)
        except ValueError as b:
            print(f"{b.__class__.__name__}: {b}")
            continue
        except WordLengthError as c:
            print(f"{c.__class__.__name__}: {c}")
            continue
        else:
            if words_main is None:
                print("Unexpected Error. Please try again...")
                continue

            print(words_main)
            break

