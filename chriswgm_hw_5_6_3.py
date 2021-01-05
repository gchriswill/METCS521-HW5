"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/10/2020
Homework Problem: #5.6.3
Description: A program that ask the user for 3 numbers, apply a calculation and
prints the results.


"""


def validate_numbers_format(input_params):
    """
    A function for validating the input of the user
    :param input_params: A string for evaluation
    :return: A list with the numbers for to be calculated.
    """

    # Checks if the input from the user is empty
    if len(input_params) <= 0:
        raise ValueError("Input was empty. Please try again...")

    # Get the numbers from the string into a list
    number_list = [int(n) for n in str(input_params) if n.isnumeric()]

    # Checks if there are 3 numbers
    if not len(number_list) == 3:
        raise ValueError("Input does not contains 3 numbers. "
                         "Please try again...")

    # Returns the list with the numbers
    return number_list


if __name__ == '__main__':

    # Loop to recollect user input if program founds error
    while True:
        str_input = input("Please enter 3 numbers, each separated by a "
                          "delimiter...")

        try:
            numbers_input = validate_numbers_format(str_input)
            result = (numbers_input[0] / numbers_input[1]) + numbers_input[2]
            break
        except ValueError as v:
            print("{} with message: {}".format(v.__class__.__name__, v.args[0]))
        except ZeroDivisionError as z:
            print("{} with message: {}. Don't use `0` for your second number. "
                  "Please try again...".format(z.__class__.__name__, z.args[0]))

    print("Calculation with result: ({} / {}) + {} = {}"
          .format(numbers_input[0], numbers_input[1], numbers_input[2],
                  result))






