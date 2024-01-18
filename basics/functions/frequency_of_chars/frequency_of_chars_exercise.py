
def char_frequency(in_str:str)->dict[str,int]:
    """Count the frequency of characters in a given string and return this statistics in a Map"""
    pass 


if __name__ == '__main__':

    # Verify implementation
    expected = {'a': 1, ' ': 4, 'e': 1, 'g': 1, 'i': 4, 'h': 1, 'm': 1, 'l': 1, 'n': 1, 'p': 1, \
        's': 4, 'r': 1, 'T': 1, '.': 1, 't': 1}
    actual = char_frequency("This is a simple string.")
    assert expected == actual
