# 17. What is the difference between copy.copy() and copy.deepcopy()?

import copy

old_spam = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_spam = copy.copy(old_spam)

old_spam[1][1] = 'AA'
new_spam[1][2] = 'BB'

print("Old Spam:", old_spam) # Old Spam: [[1, 1, 1], [2, 'AA', 'BB'], [3, 3, 3]]
print("New Spam:", new_spam) # New Spam: [[1, 1, 1], [2, 'AA', 'BB'], [3, 3, 3]]

 
old_spam = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_spam = copy.deepcopy(old_spam)

old_spam[1][1] = 'AA'
new_spam[1][2] = 'BB'

print("Old Spam:", old_spam) # Old Spam: [[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print("New Spam:", new_spam) # New Spam: [[1, 1, 1], [2, 2, 'BB'], [3, 3, 3]]