import sys

birthdays = {'Alice' : 'April 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}

try:
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is your brithday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

except KeyboardInterrupt:
    sys.exit()