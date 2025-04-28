# import re

# # Sample text
# text = "My email is john.doe123@example.com and my phone number is 123-456-7890."

# # 1️⃣ Matching a Pattern (check if a word exists)
# pattern = r'\bemail\b'
# match = re.search(pattern, text)
# if match:
#     print("1️⃣ Found the word:", match.group())
# else:
#     print("1️⃣ Word not found.")

# # 2️⃣ Searching for an Email Address
# email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
# email_match = re.search(email_pattern, text)
# if email_match:
#     print("2️⃣ Found an email:", email_match.group())
# else:
#     print("2️⃣ No email found.")

# # 3️⃣ Finding All Phone Numbers
# phone_pattern = r'\d{3}-\d{3}-\d{4}'
# phone_matches = re.findall(phone_pattern, text)
# print("3️⃣ Found phone numbers:", phone_matches)

# # 4️⃣ Replacing Email with [EMAIL]

# replaced_text = re.sub(email_pattern, '[EMAIL]', text)
# print("4️⃣ After replacement:", replaced_text)
# print(text)



a=int("25",10)
print(a)