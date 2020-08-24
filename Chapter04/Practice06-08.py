# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

bacon = [3.14, 'cat', 11, 'cat', True]


# 6. What does bacon.index('cat') evaluate to?
print(bacon.index('cat')) # 1

# 7. What does bacon.append(99) make the list value in bacon look like?
print(bacon.append(99)) # None

# 8. What does bacon.remove('cat') make the list value in bacon look like?
bacon.remove('cat')
print(bacon) # [3.14, 11, 'cat', True, 99]
