import pyperclip,re

text = str(pyperclip.paste())   
result = []                     

def PhoneNumber():
    PhnNumregex= re.compile(r'''
        (\d{3}|\(\d{3}\))    
        (\s|-|\.)?           
        (\d{3}|\(\d{3}\))    
        (\s|-|\.)?           
        (\d{4}|\(\d{4}\))    
    ''', re.VERBOSE)
    for num in PhnNumregex.findall(text):
        result.append(num[0] + num[2] + num[4])

def Email():
    emailregex = re.compile(r'''
        [a-zA-Z0-9.+_-]+  
        @                 
        [a-zA-Z0-9.+_-]+  
        \.                
        [a-zA-Z]          
        \.?               
        [a-zA-Z]*         
    ''',re.VERBOSE)

    for emails in emailregex.findall(text):
        result.append(emails)

def PrintResult():
    if len(result)>0 :
        print('Found ' + str(len(result)) + ' results:')
        for n in range(0,len(result)):
            print(result[n])
    else:
        print('No phone number or email address found.')

def main():
    PhoneNumber()
    Email()
    PrintResult()

if __name__ == '_main_':
    main()

"""import pyperclip, re

phoneRegex = re.compile(r'''(
 (\d{3}|\(\d{3}\))? # area code
 (\s|-|\.)? # separator
 (\d{3}) # first 3 digits
 (\s|-|\.) # separator
 (\d{4}) # last 4 digits
 (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
 )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9.-_%+]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-z]{2,4})   # .country
    )''', re.VERBOSE)


# find matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])   # group 0 matches entire expression

if len(matches) > 0:
    pyperclip.copy('\\n'.join(matches))
    print('Copied to clipboard:')
    print('\\n'.join(matches))
else:
    print('Neither phone numbers nor email addresses were found.')

"""



