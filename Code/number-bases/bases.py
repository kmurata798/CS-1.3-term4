#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from any base (2 up to 36)
    decoded = 0
    strings = string.digits + string.ascii_lowercase
    print(strings)
    digits = digits[::-1]
    # digits = digits[::-1] which is reverse ordering of 

    for i, number in enumerate(digits):
        decoded += base**i * strings.index(number)
        #enumerate adds a counter and an iterable, so the i and number will increase as loop continues

    return decoded


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in hexadecimal (base 16)
    # given_num = 75
    # given_num = 144
    # first_num = 0
    # second_num = 0

    # remainder = given_num % 16
    # given_num = int(given_num / 16)

    # first_num = given_num
    # print("first_num= " + str(first_num))
    # second_num = remainder
    # print("second_num= " + str(second_num))
    # if second_num > 9:
    #     if second_num == 10:
    #         second_num = 'A'
    #     elif second_num == 11:
    #         second_num = 'B'
    #     elif second_num == 12:
    #         second_num = 'C'
    #     elif second_num == 13:
    #         second_num = 'D'
    #     elif second_num == 14:
    #         second_num = 'E'
    #     elif second_num == 15:
    #         second_num = 'F'
    # if first_num > 9:
    #     if first_num == 10:
    #         first_num = 'A'
    #     elif first_num == 11:
    #         first_num = 'B'
    #     elif first_num == 12:
    #         first_num = 'C'
    #     elif first_num == 13:
    #         first_num = 'D'
    #     elif first_num == 14:
    #         first_num = 'E'
    #     elif first_num == 15:
    #         first_num = 'F'
    # print("0x" + str(first_num) + str(second_num))

    encoded = ''
    strings = string.digits + string.ascii_lowercase
    p = 0
    if number == 0:
        return 0
    
    while (base**p) <= number:
        p += 1

    while p > 0:
        print('p:', p)
        div = int(number/(base**(p-1)))
        print('div:', div)
        convert = min(div, (base-1))
        print('convert', convert)
        encoded += strings[convert]
        print('encoded', encoded)
        number = number - ( convert * base**(p-1))
        print('#', number)
        p -= 1
        print('p',p)

    return encoded


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(str(digits), base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
