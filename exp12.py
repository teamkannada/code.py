import re
text="Government First Grade College Dharwad"
match=re.search("College",text)
if match:
    print("found:", match.group())
else:   
    print("not found")