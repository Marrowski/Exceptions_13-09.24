#Завдання 5
kind_of_sport = {
    1: 'Basketball',
    2: 'Volleyball',
    3: 'Football',
    4: 'Tennis',
    5: 'Ice Hockey'
}

coach_team = {
    'Yakovenko Oleh': 'Basketball',
    'Ivanenko Oleksandr': 'Football',
    'Yemelianova Daria': 'Tennis',
    'Chobotaryov Volodymyr': 'Basketball',
    'Nedavniy Vyacheslav': 'Ice Hockey'
}

training_schedule = {
    'Basketball': '10:00 - 12:00',
    'Volleyball': '14:00 - 16:00',
    'Football': '18:00 - 20:00',
    'Tennis': '9:00 - 11:00',
    'Ice Hockey': '17:00 - 19:00'
}

training_price = {
    'Basketball': '650',
    'Volleyball': '400',
    'Football': '600',
    'Tennis': '320',
    'Ice Hockey': '470'
}

class TrainingException(Exception):
    @classmethod
    def new_exception(cls):
        return 'The key hasn`t been found.'


exception1 = TrainingException

while True:
    print('1 - Available kinds of sport')
    print('2 - Our coaches')
    print('3 - Training schedule')
    print('4 - Training prices')
    print('5 - Find coach')
    print('6 - Exit program')

    user_input = int(input('Choose what do you want:'))
    if user_input == 1:
        print(kind_of_sport)

    elif user_input == 2:
        print(coach_team)

    elif user_input == 3:
        print(training_schedule)

    elif user_input == 4:
        print(training_price)

    elif user_input == 5:
        coach = input('Input name of coach:')
        try:
            if coach in coach_team:
                print(coach_team.get(coach))
            else:
                raise TrainingException()
        except TrainingException as e:
            print('Unknown key.')

    elif user_input == 6:
        print('Goodbye!')
        break

    else:
        raise ValueError('Unknown action.')
