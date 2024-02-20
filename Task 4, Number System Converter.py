"""
This program converts between decimal, binary, and hexadecimal integers

The conversion formula for decimal to binary was modelled off of this article: https://www.splashlearn.com/math-vocabulary/decimal-to-binary#:~:text=Here%20are%20the%20steps%20for,get%200%20as%20the%20quotient.
The conversion formula for decimal to hexadecimal was modelled off of this article: https://www.geeksforgeeks.org/decimal-to-hex-converter/
"""

print("""                   
▄▄▄ ▄▄▄ ▄▄▄

█▀▄ █▀▀ █▀▀
█ █ █▀▀ █
▀▀  ▀▀▀ ▀▀▀
█▀▄ ▀█▀ █▀█
█▀▄  █  █ █
▀▀  ▀▀▀ ▀ ▀
█ █ █▀▀ █ █
█▀█ █▀▀ ▄▀▄
▀ ▀ ▀▀▀ ▀ ▀
▄▄▄ ▄▄▄ ▄▄▄
""")

number_system = str(input("Which would you like to convert from? "))   # User enters which number format they wish to convert from


# This function converts decimal numbers to binary
def decimal_to_binary(decimal_number):
    binary_converted_number = 0   # Records the converted hexadecimal number
    remainders = []   # Creates a list to record the remainders from the division process

    # Repeats steps 1-3 for base 2
    while decimal_number > 0:
        remainders.append(decimal_number % 2)
        decimal_number //= 2

    place_value = 0   # Records the place value of each converted 0 and 1
    for number in remainders:
        # This addition process naturally reverses the order of the remainders as each place value of 1 is a multiple of 10
        binary_converted_number += number * (10 ** place_value)
        place_value += 1

    # Adds 0s to the front of the binary if the length of the number is not a multiple of 4
    if not len(str(binary_converted_number)) % 4 == 0:
        binary_converted_number = ''.join(((4 - len(str(binary_converted_number)) % 4) * '0', str(binary_converted_number)))

    return binary_converted_number   # Returns the converted binary number


# Creates a dictionary allowing for the conversion from decimal digits to hexadecimal characters
hexadecimal = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'
}


# This function converts decimal numbers to hexadecimal
def decimal_to_hex(decimal_number):
    converted_hex_number = []    # Creates a list to record the converted hexadecimal number
    remainders = []   # Creates a list to record the remainders from the division process

    # Repeats steps 1-3 for base 16
    while decimal_number > 0:
        remainders.append(decimal_number % 16)
        decimal_number //= 16

    # Converts the remainders into hexadecimal characters
    for number in remainders:
        converted_hex_number.append(hexadecimal[str(number)])

    converted_hex_number.reverse()   # Reverses the list of hexadecimal characters
    converted_hex_number = ''.join(converted_hex_number)   # Joins the list of hex characters into a string

    return converted_hex_number   # Returns the converted hexadecimal number


# This function converts binary numbers to decimal
def binary_to_decimal(binary_number):
    converted_decimal_number = 0   # Records the converted hexadecimal number

    place_values = len(binary_number) - 1   # Records the number of digits/place values in the binary number``

    # This loop converts the binary to decimal
    for digit in binary_number:
        # For every 1 in the binary, 2^(its place value) is added the decimal number
        if digit == '1':
            converted_decimal_number += 2 ** place_values

        place_values -= 1

    return converted_decimal_number   # Returns the converted decimal number


# This function converts hexadecimal numbers to decimal
def hex_to_decimal(hex_number):
    hex_number = list(hex_number)   # Separates the characters of the hexadecimal number into its characters

    hexadecimal_keys = list(hexadecimal)   # Creates a list of the keys from the hexadecimal dictionary
    hexadecimal_values = list(hexadecimal.values())   # Creates a list of the values from the hexadecimal dictionary

    place_value = 0   # Records the place value of the character being converted
    for number in hex_number:
        # Converts the hexadecimal character to its corresponding decimal number
        hex_number[place_value] = hexadecimal_keys[hexadecimal_values.index(number.upper())]
        place_value += 1

    converted_decimal_number = []   # Creates a list to record the decimal number
    hex_number.reverse()   # Reverse the hex_number list

    place_values = len(hex_number)
    # Converts the digits in the placeholders to decimal by multiplying by 16^(place value)
    for place_value in range(place_values):
        converted_decimal_number.append(int(hex_number[place_value]) * (16 ** place_value))

    converted_decimal_number = sum(converted_decimal_number)   # Adds the values in the placeholders to one decimal number

    return converted_decimal_number   # Returns the converted decimal number


# This block of code handles inputs, calls the functions to convert the numbers, and prints the results
if number_system.upper() == "DEC":
    decimal_number = int(input("Enter a decimal number: "))   # User enters a decimal number to be converted

    # Calls functions to convert the decimal number
    binary_number = decimal_to_binary(int(decimal_number))
    hex_number = decimal_to_hex(int(decimal_number))

    print(f"Binary of {decimal_number}: {binary_number}\nHexadecimal of {decimal_number}: {hex_number}")   # Prints the conversion

elif number_system.upper() == "BIN":
    binary_number = str(input("Enter a binary number: "))   # User enters a binary number to be converted

    # Calls functions to convert the binary number
    decimal_number = binary_to_decimal(binary_number)
    hex_number = decimal_to_hex(int(decimal_number))

    print(f"Decimal of {binary_number}: {decimal_number}\nHexadecimal of {binary_number}: {hex_number}")   # Prints the conversion

elif number_system.upper() == "HEX":
    hex_number = str(input("Enter a hexadecimal number: "))   # User enters a hexadecimal number to be converted

    # Calls functions to convert the hexadecimal number
    decimal_number = hex_to_decimal(hex_number)
    binary_number = decimal_to_binary(int(decimal_number))


    print(f"Decimal of {hex_number}: {decimal_number}\nBinary of {hex_number}: {binary_number}")   # Prints the conversion
