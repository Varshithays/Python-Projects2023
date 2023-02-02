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

if __name__ == '__main__':
    main()





