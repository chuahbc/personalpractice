# 5. If a dictionary is stored in spam, what is the difference between 
# the expressions 'cat' in spam and 'cat' in spam.keys()?

spam = {'cat':20}

print(spam['cat']) # 20
print(spam.keys()) # dict_keys(['cat'])