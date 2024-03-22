# Tuple objects

# Tuples can be defined with or without surrounding parentheses
squares = (1, 4, 9, 16, 25)
assert squares == (1, 4, 9, 16, 25)     # == compares element by element
print(type(squares))

# Empty tuples are constructed by an empty pair of parentheses
empty = ()
assert empty == ()

# A tuple with one item is constructed by following a value with a comma
singleton = 'hello',    # <-- note trailing comma
assert singleton == ('hello',)

# Tuple packing
t = 1, 4, 9
assert (1, 4, 9) == t
# Tuple unpacking
x, y, z = t
assert 1 == x
assert 4 == y
assert 9 == z

# Concatination
assert (1, 2, 3, 4, 5, 6, 7) == (1, 2, 3, 4) + (5, 6, 7)

# Indexing
squares = (1, 4, 9, 16, 25)
assert 1 == squares[0]
assert 25 == squares[-1]

# Tuples are immutable, thus, we cannot change their elements!

# Slicing
squares = (1, 4, 9, 16, 25)
assert (4,9) == squares[1:3]
assert (1,4,9) == squares[:3]
assert (16, 25) == squares[3:]

# Length of a tuple
squares = (1, 4, 9, 16, 25)
assert len(squares) == 5

# Nested tuples
a = ('a', 'b', 'c')
n = (1, 2, 3)
nested = (a, n)
assert (('a', 'b', 'c'), (1, 2, 3)) == nested

