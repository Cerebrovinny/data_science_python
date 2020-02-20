secret_number = 9
i = 0
while i < 3:
    guess = int(input('Guess: '))
    i += 1
    if guess == 9:
        print('You win')
        break
else:
    print('Sorry you failed')