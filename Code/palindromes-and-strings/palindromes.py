#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    extra = " ?!,.;:-_'"
    for index in extra:
        text = text.replace(index, '')
    first_pt = 0
    second_pt = len(text) - 1
    if len(text) < 1:
        return True

    while first_pt <= second_pt:
        if text[first_pt].lower() != text[second_pt].lower():
            return False
        first_pt += 1
        second_pt -= 1
    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here

    # First time through the function call
    # Initialize left and right boundaries
    if left == None:
        left = 0 
    
    if right == None:
        right = len(text) - 1

    # Check if left boundary crosses or meets with right boundary
    if left >= right:
        return True
    
    # base cases:
    # Check that the left and right elements are chars, if not, then skip the element and update left or right with next element
    if text[left].isalpha() is not True:
        return is_palindrome_recursive(text, left + 1, right)
    
    if text[right].isalpha() is not True:
        return is_palindrome_recursive(text, left, right - 1)

    # Matching chars:
    # Check whether each letter matches the other
    if text[left].lower() != text[right].lower():
        return False 
    
    # Recursive call:
    # Loop case: as long as the left boundary is less than the right, we have not searched through the entire string
    if left < right: 
        return is_palindrome_recursive(text, left + 1, right - 1)
    
    return True 
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
