# Author:         Zulkifli Salami
# Program:        Password Generator
# Date Created:   01-24-23
# Date Modified:  01-27-23
# Description: A program to generate a random strong password based on a user's instructions. User decides the number of characters for
# password, also the number of letters, digits, and special characters in the custom password. The program should be tested to all the extremes to 
# ensure proper functioning


# pythom imports to use string and random module
import random
import string


# declare variables for the random string constants to be used in the password
all_letters_capital = string.ascii_uppercase
all_letters_lowercase = string.ascii_lowercase
all_digits = string.digits
all_special_characters = string.punctuation

# constants
MINIMUM = 0
CHARACTER_LENGTH = 8
length_of_letters = 0
length_of_digits = 0
length_of_special_characters = 0





# function for input validation
def input_validation(type, MAXIMUM_VALUE):
# initialize a condition to get valid input from user for number of letters in password
    need_input_2 = True
    # Set a condition for valid input 
    while need_input_2:
        # Prompt the user for input and store it as a integer
        try:
            user_input = int(input(F'\nPlease specifiy the number of {type} for your password: '))
            # Determine if input is valid
            if user_input < MINIMUM or user_input > MAXIMUM_VALUE:
                # Dispaly error message
                print(f'Error !! The input has to be in the range 0 and {MAXIMUM_VALUE}. Kindly try again, Thank you :)\n')
            # Continue program if valid
            else:
                need_input_2 = False
        # Display error message if not successfully stored as integer
        except:
            print('Error !! The input has to be a whole number. Decimals, alphabets and special characters not accepted. Kindly try again, Thank you :)\n')
    return user_input
    

# Function to generate a random password
def password_generator (value1, value2, value3, value4):
    result_upper_case = random.choice(all_letters_capital)
    result_lower_case = ''.join(random.choice(all_letters_lowercase) for letter in range(value2 - 1))
    result_digits = ''.join(random.choice(all_digits) for digit in range(value3))
    result_special_characters = ''.join(random.choice(all_special_characters) for special_character in range(value4))
    for char in range (value1):
        print (f'\nYour desired password is: \n{result_upper_case}{result_lower_case}{result_digits}{result_special_characters}')
        break





# Input
# initialize a condition to get valid input from user for length of characters in password
need_input = True
# Set a condition for valid input 
while need_input:
    # Prompt the user for input and store it as a integer
    try:
        length_of_characters = int(input('\nPlease specifiy the length of characters for your password: '))
        if length_of_characters < CHARACTER_LENGTH:
            # Dispaly error message if less than 8
            print('Error !! The input has to be greater than or equal to 8. Kindly try again, Thank you :)\n')
        # Continue program if greater than 8
        else:
            need_input = False
    # Display error message if not successfully stored as integer
    except:
        print('Error !! The input has to be a whole number. Decimals, alphabets and special characters not accepted. Kindly try again, Thank you :)\n')
    


# Call the input validation function into a variable using type and maximum value
need_input_3 = True
while need_input_3:
    letters = input_validation('letters', length_of_characters)
    length_of_digits = length_of_characters - letters
    digits = input_validation('digits', length_of_digits)
    length_of_special_characters = length_of_digits - digits
    special_characters = input_validation('special characters', length_of_special_characters)
    # Determine if total number of individual character type is equal to users desired character length
    total_character_type = letters + digits + special_characters
    if total_character_type != length_of_characters:
        print(f'The total letters, digits and special characters i.e., {letters, digits, special_characters} has to be equal to your desired character length i.e., {length_of_characters}. Kindly try again, Thank you :)\n')
    else:
        need_input_3 = False


# Pass the users desired instructions into a function that generates random password and prints out the password 
password_generator(length_of_characters,letters,digits,special_characters)
