# Strings
assert "Python" == 'Python'

s = "Python\nLanguage"
print(type(s))
print(s)

r = r"Python\nLanguage"
print(type(r))
print(r)

m = """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to    
"""
print(type(m))
print(m)


# Concationation
assert 3 * 'un' + 'ium' == 'unununium'
assert "Python " "Language" == "Python Language"

# Indexing
word = "Python"
assert "P" == word[0]
assert "n" == word[5]
assert "n" == word[-1]
assert "P" == word[-6]
# word[0] = "X" Error: strings are  are immutable!!

# Slicing
word = "Python"
assert "Py" == word[0:2]    # [0,2)
assert "tho" == word[2:5]   # [2,5)

assert "Py" == word[:2]     # [0,2)
assert "thon" == word[2:]   # [2,6)

# Length of a string
assert len("supercalifragilisticexpialidocious") == 34


# Conversions

assert 7 == int("7")
assert 3.14 == float("3.14")

assert "13" == str(13)
assert "3.14" == str(3.14)
