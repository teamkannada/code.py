import re
pattern='a...s$'
test_string='456s'
result=re.match(pattern,test_string)
if result:
    print("search successful")
else:
    print("search unsuccessful")