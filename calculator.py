#Завдання 2
def addition(num_1: int, num_2: int):
    return num_1 + num_2


def subtraction(num_1: int, num_2: int):
    return num_1 - num_2


def multiplication(num_1: int, num_2: int):
    return num_1 * num_2


def division(num_1: int, num_2: int):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('Sorry, but you can`t divide on zero.')
        return 'Error'

def power(num_1: int, num_2: int):
    try:
        return num_1 ** num_2
    except ZeroDivisionError:
        print('You cant power zero in negative.')
        return 'Error'

while True:
    math_sign = input('Input math sign:')
    if math_sign == '+':
        num_1 = int(input('Input first number:'))
        num_2 = int(input('Input second number:'))
        print(addition(num_1, num_2))

    elif math_sign == '-':
        num_1 = int(input('Input first number:'))
        num_2 = int(input('Input second number:'))
        print(subtraction(num_1, num_2))

    elif math_sign == '*':
        num_1 = int(input('Input first number:'))
        num_2 = int(input('Input second number:'))
        print(multiplication(num_1, num_2))

    elif math_sign == '/':
        num_1 = int(input('Input first number:'))
        num_2 = int(input('Input second number:'))
        print(division(num_1, num_2))

    elif math_sign == '**':
        num_1 = int(input('Input first number:'))
        num_2 = int(input('Input second number:'))
        print(power(num_1, num_2))
    else:
        raise ValueError('Invalid user input.')
