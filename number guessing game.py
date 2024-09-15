import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def no_guesses(attempts,i):
    if attempts - i != 0:
        print('guess again')
        return (f"you have {attempts - i} attempts remaining to guesses the number")
    else:
        return ('you are out of guesses,you lose!!')
def easy_hard(choose_num,attempts):
    print(f"you have {attempts} attempts remaining to guess the number!")
    for i in range(1,attempts + 1):
        guess = int(input('make a guess'))
        if guess > choose_num:
            print('your guess is too high')
            print(no_guesses(attempts,i))
        elif guess < choose_num:
            print('your guess is too low')
            print(no_guesses(attempts,i))
        else:
            print(f'you guess is right...The answer was {choose_num}')
            break
print()
print('let me think of a number between 1 to 50.')
num_list = list(range(51))
choose_num = random.choice(num_list)
while True:
    level = input("Choose level of difficulty...Type 'easy' or 'hard' : ")
    if level == 'easy':
        easy_hard(choose_num,attempts = 10)
        break
    elif level == 'hard':
        easy_hard(choose_num,attempts = 5)
        break
    else:
        print("you've entered wrong input,Try again")