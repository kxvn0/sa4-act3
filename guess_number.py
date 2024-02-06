number = 10

print('I am thinking of a number....')
while True:

    guess = (int(input('What number am I thinking of?')))
    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    if guess < number:
        print('Sorry! The number you entered is too low. Try again:  ')
    elif guess > number:
        print('Sorry! The number you entered is too high. Try again:  ')


