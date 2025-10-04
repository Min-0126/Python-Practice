#this is a guess the number game
#Import moduel 'random'
import random

#random.radiant can be used by import random module
#Select a number between 1 and 20
secret_number = random.randint(1,20)
print('I am thinking of a nuber between 1 and 20')

#Ask the player to guess 6 times (7-1)
for guess_taken in range(1,7):
    print('Take a guess')
    guess = int (input('>'))

    if guess < secret_number:
        print("Guess is low")
    elif guess > secret_number:
        print('Guess is high')
    else:
        break   #Guess is correct

if guess == secret_number:
    print('Good job. You got it in ' + str(guess_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))

