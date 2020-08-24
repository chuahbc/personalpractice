# 10. What is the difference between the append() and insert() list methods?

# append() adds the item to the end of the list

spam = [1,2,3,4]
spam.append('howdy')
print(spam) # [1, 2, 3, 4, 'howdy']

spam.insert(2,100)
print(spam) # [1, 2, 100, 3, 4, 'howdy']