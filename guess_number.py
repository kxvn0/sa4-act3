number = 10

print('I am thinking of a number....')
while True:

    guess = (int(input('What number am I thinking of?')))
    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    else:
        print('Sorry! That is not the right number. Try again: ')


