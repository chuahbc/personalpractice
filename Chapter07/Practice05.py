# 5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)',
# what does group 0 cover? Group 1? Group 2?

import re

message = '000-000-0000'

isPhoneNumber = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = isPhoneNumber.search(message)

print(mo.group()) # 000-000-0000
print(mo.group(1)) # 000
print(mo.group(2)) # 000-0000