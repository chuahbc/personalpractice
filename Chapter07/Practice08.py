# 8. What does the | character signify in regular expressions?

# or

import re

isAlpha = re.compile(r'aaa|bbb')

message = 'cccaaaccc'
mo1 = isAlpha.search(message)


message = 'cccbbbccc'
mo2 = isAlpha.search(message)

print(mo1.group()) # aaa
print(mo2.group()) # bbb