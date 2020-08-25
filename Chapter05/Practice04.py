# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

spam = {'bar': 100}

print(spam['foo']) # KeyError: 'foo'
print(spam['bar']) # 100
