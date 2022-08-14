# This is a Guess the Number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1,20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

for guessesTaken in range(6):
    print ('Enter your guessed number')
    guess = input()
    guess = int(guess)
    if guess > number:
        print('You are too high')
    if guess < number:
        print('You are too low')
    if guess == number:
        break
if guess == number:
    
    print('Congradulations ' + myName + ' you guessed my number in ' + str(guessesTaken + 1) + ' tries')

if guess != number:
    number = str(number)
    
    print('Sorry ' + myName + " you didn't guessed my number in " + str(guessesTaken + 1) + ' tries')
    print('The number I was thinking about was ' + number) 
    

