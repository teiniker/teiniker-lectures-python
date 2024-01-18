def is_palindrome(in_str:str)->bool:
    """Check if the given string is a palindrome."""
    for i in range(0, int(len(in_str)/2)):       # Run loop from 0 to len/2
        if in_str[i] != in_str[len(in_str)-i-1]:
            return False
    return True


if __name__ == '__main__':

    # Verify implementation
    assert is_palindrome('00')
    assert not is_palindrome('011')
    assert is_palindrome('000010000')

    assert is_palindrome('otto')
    assert is_palindrome('amanaplanacanalpanama') # A man, a plan, a canal - Panama
