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
    # # "Cheating" way
    # #1 get each digit
    # decimal_num = 0
    # digits = digits[::-1]
    # for i in range(len(digits)):
    #     digit = int(digits[i], base=base)
    #     decimal_num += digits * base ** i
    # return decimal_num

    # TODO: Decode digits from any base (2 up to 36)
    print("::DECODE() start::")
    decoded = 0
    strings = string.digits + string.ascii_lowercase
    print(strings)
    digits = digits[::-1]
    # digits = digits[::-1] which is reverse ordering of 

    for i, number in enumerate(digits):
        print("i: ", i)
        print("number: ", number)
        print("strings.index(number)", strings.index(number))
        print("strings: ", strings)
        decoded += base**i * strings.index(number)
        #enumerate adds a counter and an iterable, so the i will increase as we loop each number
        print("decoded: ", decoded)
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

    print("::ENCODE start::")
    encoded = ''
    strings = string.digits + string.ascii_lowercase
    p = 0
    if number == 0:
        return 0
    # If user wants to convert to base 10, immediately return decoded number (which is already in base 10)
    elif base == 10:
        return number
    
    while (base**p) <= number:
        p += 1

    while p > 0:
        print('p:', p)
        div = number//(base**(p-1))
            #1st 12 / 8 = 1.5 ==> 1
            #2nd 4 / 4
        print('div:', div)
        convert = min(div, (base-1))
            # 1 = 1 ==> 1
        print('convert:', convert)
        encoded += strings[convert]
            # 0[1]234... ==> 1
        print('encoded:', encoded)
        number = number - ( convert * base**(p-1))
            # 12 - ( 1 * 2**3 ) = 12 - 8 = 4
        print('#: ', number)
        p -= 1

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

    print("::CONVERT start::")
    # Convert digits string to all LOWERCASE words to avoid error if user inputs capital letters for base 16 numbers
    return encode(decode(str(digits).lower(), base1), base2)


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
