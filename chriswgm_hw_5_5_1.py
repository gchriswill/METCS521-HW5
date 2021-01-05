"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/10/2020
Homework Problem: #5.5.1
Description: A program that ask the user for a sentence, checks the total
vowels and consonants in the sentences and prints the results.


"""

import string

INPUT_ASK = "Enter an English sentence:"

VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_letters.lower()).difference(set(VOWELS)))


def vc_counter(str_sentence):
    """
    A function for counting vowels and consonants
    :param str_sentence: A string for evaluation
    :return: A dictionary with keys as the total counts and values as
    the result of the letters found.
    """

    # Filtering the vowels from param string
    vowels = "".join([str(c) for c in str_sentence if c in VOWELS])

    # Filtering the consonants from param string
    consonants = "".join([str(c) for c in str_sentence if c in CONSONANTS])

    # Returning dictionary with total values of filters
    return {"total_vowels": len(vowels), "total_consonants": len(consonants)}


if __name__ == '__main__':

    # Collecting user input
    str_input = input("Enter an English sentence:")

    # Loop to recollect user input if program founds error
    while True:
        if len(str_input) <= 0:
            print("Input was empty")
            str_input = input(INPUT_ASK)
        else:
            break

    dict_result = vc_counter(str_input.lower())

    print("Input Sentence: {}".format( str_input))

    print("Total # of vowels in sentence: {}"
          .format(dict_result["total_vowels"]))

    print("Total # of consonants in sentence: {}"
          .format(dict_result["total_consonants"]))
