# 11. What are two ways to remove values from a list?

# del Statements

spam = ['A','B','C','D']
del spam[2]
print(spam) # ['A', 'B', 'D']


# .remove()

spam.remove('A')
print(spam) # ['B', 'D']
