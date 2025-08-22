import random

while True:
    hearts = 5
    firstNumber = random.randint(1,9999)
    secondNumber = random.randint(1,9999)
    operations = ['+', '-', '*', '/', '%']
    operation = random.choice(operations)
    while hearts > 0:
        result = int(eval(f'{firstNumber}{operation}{secondNumber}'))
        if operation == '/':
            print(f'please enter without decimals')
        try:
            userAnswer = int(input(f'{firstNumber} {operation} {secondNumber}: = '))
        except ValueError:
            print('there is a problem\nplease enter numbers only\nwithout decimals and symbols')
        else:
            if userAnswer == result:
                print('your answer is correct')
                print(f'you had {hearts} more')
                break
            else:
                hearts = hearts - 1
                print('your answer is incorrect, try again')
                print(f'Hearts: {hearts}')
                if hearts == 0: print('you lose the step, correct answer is ', result)
