"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 08/10/2020
Homework Problem: #5.5.2
Description: A program that take user input with date and time format, validates
this input and prints out the result


"""


DATE_KEYS = ["month", "day", "year"]
TIME_KEYS = ["hour", "minute", "second"]


def is_validate_datetime(date_time_param: str):

    # Initial format validation Stack
    if len(date_time_param) is not 19:
        return False, "Date format length must be of 19 characters"

    slash_occurrences = date_time_param.count("/")
    colon_occurrences = date_time_param.count(":")
    space_occurrences = date_time_param.count(" ")

    expected_delimiters_format = slash_occurrences == 2 \
                                 and colon_occurrences == 2 \
                                 and space_occurrences == 1

    if not expected_delimiters_format:
        return False, "Format must include delimiters: MM/DD/YYYY HH:mm:SS"


    # Date validation conditional stack
    date_string = dict(zip(DATE_KEYS, date_time_param.split()[0].split("/")))
    if not len(date_string[DATE_KEYS[0]]) is 2:
        return False, "Months must be of 2 numbers and with leading zero if " \
                      "less than 10"

    if int(date_string[DATE_KEYS[0]]) > 12 \
            or int(date_string[DATE_KEYS[0]]) <= 0:
        return False, "Months can not be greater than 12 or less/equal than 0"

    if not len(date_string[DATE_KEYS[1]]) is 2:
        return False, "Days must be of 2 numbers and with leading zero if " \
                      "less than 10"

    if int(date_string[DATE_KEYS[1]]) > 28 \
            or int(date_string[DATE_KEYS[1]]) <= 0:
        return False, "Days can not be greater than 28 or less/equal than 0"

    if not len(date_string[DATE_KEYS[2]]) is 4:
        return False, "Years must be of 4 numbers"

    if int(date_string[DATE_KEYS[2]]) <= 0:
        return False, "Years can not be less/equal than 0"


    # Time validation conditional stack
    time_string = dict(zip(TIME_KEYS, date_time_param.split()[1].split(":")))

    if not len(time_string[TIME_KEYS[0]]) is 2:
        return False, "Hours must be of 2 numbers and with leading zero if " \
                      "less than 10"

    if int(time_string[TIME_KEYS[0]]) > 23 \
            or int(time_string[TIME_KEYS[0]]) < 0:
        return False, "Hours can not be greater than 23 or less/equal than 0"

    if not len(time_string[TIME_KEYS[1]]) is 2:
        return False, "Minutes must be of 2 numbers and with leading zero " \
                      "if less than 10"

    if int(time_string[TIME_KEYS[1]]) > 59 \
            or int(time_string[TIME_KEYS[1]]) <= 0:
        return False, "Minutes can not be greater than 59 or less/equal than 0"

    if not len(time_string[TIME_KEYS[2]]) is 2:
        return False, "Seconds must be of 2 numbers and with leading zero if " \
                      "less than 10"

    if int(time_string[TIME_KEYS[2]]) > 59 \
            or int(time_string[TIME_KEYS[2]]) <= 0:
        return False, "Seconds can not be greater than 59 or less/equal than 0"

    return True, None


if __name__ == '__main__':

    while True:

        str_input = input("Enter a date time in 24 hour format "
                          "(MM/DD/YYY HR:MIN:SEC):")
        validation, message = is_validate_datetime(str_input)

        time_am_pm = \
            int(dict(zip(TIME_KEYS,
                         str_input.split()[1].split(":")))[TIME_KEYS[0]]) <= 11

        if validation:
            date_str = str_input.split()[0]
            time_str = str_input.split()[1]
            print("HR:MIN:SEC is {}".format(time_str))
            print("DD/MM/YYYY is {}".format(date_str))
            print("The time is {}".format("AM" if time_am_pm else "PM"))
            break
        else:
            print(message)
