while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        #Jump back to the start of the loop if name is not JOe
        continue        
    print('Hello, Joe. What is the password? (it is a fish.)')
    password = input('>')
    if password == 'swordfish':
        #Leavce the loop if the password is true
        break
print ('Access granted')
