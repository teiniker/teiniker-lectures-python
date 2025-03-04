# Set objects

# A set is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
assert basket == {'apple', 'orange', 'pear', 'banana'}

# To create an empty set you have to use set(), not {};
empty_set = {}
assert not empty_set

# Fast membership testing
assert 'orange' in basket
assert 'crabgrass' not in basket

# Iterate over a set
for fruit in ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']:
    assert fruit in basket
