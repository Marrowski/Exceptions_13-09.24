#Завдання 4
class MyException(Exception):
    def __init__(self, height: int, minheight: int, maxheight: int):
        self.height = height
        self.minheight = minheight
        self.maxheight = maxheight
    def __str__(self):
        return (f'Her height: {self.height} is not enough to do this task, it must be from {self.minheight} '
                f'to {self.maxheight} m.')

class Human:
    def __init__(self, name: str, age: int, height: int):
        self.__name = name
        minheight, maxheight = 165, 196
        if minheight < height < maxheight:
            self.__height = height
        else:
            raise MyException(height, minheight, maxheight)

    def output_human(self):
        return f'Her name is {self.__name}, height {self.__height}'

try:
    human1 = Human('Alice', 16, 178)
    human1.output_human()

    human2 = Human('Ivanna', 14, 155)
    human2.output_human()
except MyException as exc:
    print(exc)