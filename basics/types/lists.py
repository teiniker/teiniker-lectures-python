# List objects

squares = [1, 4, 9, 16, 25]
assert squares == [1, 4, 9, 16, 25]     # == compares element by element
print(type(squares))

# Concatination
assert [1, 2, 3, 4, 5, 6, 7] == [1, 2, 3, 4] + [5, 6, 7]

# Indexing
squares = [1, 4, 9, 16, 25]
assert 1 == squares[0]
assert 25 == squares[-1]

squares[0] = 99     # Lists are mutable!!!
assert [99, 4, 9, 16, 25] == squares

# Adding new items
squares = [1, 4, 9, 16, 25]
squares.append(6**2)
assert [1, 4, 9, 16, 25, 36] == squares

# Slicing
squares = [1, 4, 9, 16, 25]
assert [4,9] == squares[1:3]
assert [1,4,9] == squares[:3]
assert [16, 25] == squares[3:]

# Length of a list
squares = [1, 4, 9, 16, 25]
assert len(squares) == 5

# Nested lists

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

assert [['a', 'b', 'c'], [1, 2, 3]] == x
print(type(x))
