import random

keep_playing = True

while keep_playing:
    guess_number = 0
    count = 0
    magic_number = random.randint(1, 101)
    while magic_number != guess_number:
        guess_number = int(input('What is your guess?')) 
        count = count + 1
        if magic_number > guess_number:
            print('Higher')
        elif magic_number < guess_number:
            print('Lower')
        else:
            print('You guessed it!')
            print(f'it took you {count} guesses')

  
    decision = input('Do you want to keep playing (yes/no)? ').lower()
    if decision == 'yes':
        keep_playing = True

    else:
        keep_playing = False