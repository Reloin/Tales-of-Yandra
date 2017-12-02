print("Game intro line")
person = input('Enter your name: ')
print('Hello', person, '!, Welcome to the game')
valid = ['1','2','3']

def inputCheck(userChoice):
    if userChoice == '1':
        print('You Have Chosen to Enter Text to Encrypt!')
        print('1')
        exit()
    if userChoice == '2':
        print('You Have Chosen to Encypt Entered Text!')
        encryptText()
    if userChoice == '3':
        print('You Have Chosen to Display Encypted Text!')
        displayText()

while True:
    userChoice = str(input('What Would You Like To Do? '))
    if userChoice in valid:
        inputCheck(userChoice)
        break
    else:
        print('Sorry but you didn\'t choose a valid option, please try again')