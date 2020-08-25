# 6. If a dictionary is stored in spam, what is the difference between 
# the expressions 'cat' in spam and 'cat' in spam.values()?

spam = {'cat':20}

print(spam['cat']) # 20
print(spam.values()) # dict_values([20])