number = 10
num_of_guess = 4


while num_of_guess > 0:
    guess = int(input('What number am I thinking of?'))

    if guess == number:
        print('Congratulations! You guessed the right number.')
        break
    elif guess < number:
        print('Sorry! The number you entered is too low. Try again: ')
    elif guess > number:
        print('Sorry! The number you entered is too high. Try again: ')
    num_of_guess -= 1

    print(f'You have {num_of_guess} guesses left.')

if num_of_guess ==0:
    print(f'Sorry! You have run out of guesses. The number was {number}.')