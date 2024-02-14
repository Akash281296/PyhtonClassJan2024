LUCKY_NUMBER = 45  

points = 0
attempt = 0
max_attempts = 10

while True:
    attempt += 1
    print(f'\nAttempt: {attempt}')

    given_number = int(input('Enter a number between 0 and 100: '))
    if given_number == LUCKY_NUMBER:
        if attempt <= 3:
            points = 100
        elif attempt <= 9:
            points = 60
        elif attempt <=16:
            points = 20
        elif attempt <= 25:
            points = 5
        elif attempt >= 26:
            points = 0
        print(f'You guessed correctly in {attempt} attempts! Points: {points}')
        break
    elif given_number > LUCKY_NUMBER:
        print('Reduce your guessing number')
    else:
        print('Increase your guessing number')

    if attempt >= max_attempts:
        print(f'Out of attempts. The correct number was {LUCKY_NUMBER}.')
        break