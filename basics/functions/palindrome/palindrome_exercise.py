
def is_palindrome(in_str):
    """Check if the given string is a palindrome."""
    pass 


if __name__ == '__main__':

    # Verify implementation
    assert is_palindrome('00')
    assert not is_palindrome('011')
    assert is_palindrome('000010000')

    assert is_palindrome('otto')
    assert is_palindrome('amanaplanacanalpanama') # A man, a plan, a canal - Panama
