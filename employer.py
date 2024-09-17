#Завдання 3

class Employer:
    def __init__(self, name: str, surname: str, departament: str, year_start_work: int):
        self.name = name
        self.surname = surname
        self.departament = departament
        self.year_start_work = year_start_work
        if year_start_work < 1956:
            raise ValueError('You are too old for working here.')

    def print_employer(self):
        return (f'Name: {self.name}, surname: {self.surname}, departament: {self.departament}, Year of staring work:'
                f' {self.year_start_work}')

employer1 = Employer(name=input('Name:'), surname=input('Surname:'), departament=input('Departament:'), year_start_work=int(input('Input year of starting work:')))
employer2 = Employer(name=input('Name:'), surname=input('Surname:'), departament=input('Departament:'), year_start_work=int(input('Input year of starting work:')))
employer3 = Employer(name=input('Name:'), surname=input('Surname:'), departament=input('Departament:'), year_start_work=int(input('Input year of starting work:')))
employer4 = Employer(name=input('Name:'), surname=input('Surname:'), departament=input('Departament:'), year_start_work=int(input('Input year of starting work:')))

print('Our employers:')
print(employer1.print_employer())
print(employer2.print_employer())
print(employer3.print_employer())
print(employer4.print_employer())

print('Employers hired after this year:')
if employer1.year_start_work == 2024:
    print(employer1.print_employer())
if employer2.year_start_work == 2024:
    print(employer2.print_employer())
if employer3.year_start_work == 2024:
    print(employer3.print_employer())
if employer4.year_start_work == 2024:
    print(employer4.print_employer())
else:
    print('There are no new employers.')