import pyperclip, re

IndianNumber = re.compile(r'''(
(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}

)''',re.VERBOSE)


emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+       # Username
@                       # @Symbol
[a-zA-Z0-9.-]+          # Domain Name
(\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# Find Matches in Clipboard Text
text = str(pyperclip.paste())

email_groups = emailRegex.findall(text)
Indian_Contacts = IndianNumber.findall(text)

matched = []


for group in Indian_Contacts:
        phoneNum = group[0]
        matched.append(phoneNum)

for group in email_groups:
    matched.append(group[0])

if len(matched) > 0:
    pyperclip.copy('\n'.join(matched))
    print('Copied to clipboard!\n')
    print('Found ' + str(len(matched)) + ' results:')
    print('\n'.join(matched))
else:
    print('No Phone Numbers or Emails found in your website')