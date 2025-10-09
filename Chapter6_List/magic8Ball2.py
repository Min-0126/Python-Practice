import random

messages = ['It is certain',
        'It is decidely so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful'
            ]

print('Ask a yes or no quesiton: ')
input('>')
print(messages[random.randint(0, len(messages) - 1)])