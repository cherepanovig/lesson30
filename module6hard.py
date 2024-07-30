# Дополнительное практическое задание по модулю: "Наследование классов."
import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True):
        if len(sides) != self.sides_count:  # кол-во передаваемых в функцию аргументов д.б. равно sides_count (Если
            # передано неправильное количество сторон, нужно создать список [1, 1, ..., 1])
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)
        self.__color = color
        self.filled = filled

    def __is_valid_color(self, r, g, b):
        l_color = [r, g, b]
        l_color.sort()
        for i in l_color:
            if not isinstance(i, int) or not (0 <= i <= 255):
                return False
        return True

    def get_color(self):
        # res = [x for x in self.__color]
        # return res
        return list(self.__color)  # возвращает список RGB цветов

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        #return self.sides_count == len(sides) and all(isinstance(s, int) and s > 0 for s in sides)
        lst = []
        for x in sides:
            if x > 0:
                lst.append(x)
        if len(lst) > 0 and len(sides) == len(self.__sides):
            #print(len(lst), len(sides), len(self.__sides))
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__() / (2 * math.pi)

    def get_square(self):
        #return (self.__len__ ** 2) / (4 * math.pi)
        return (self.__radius() ** 2) * math.pi

    def __str__(self):
        return f"Круг с радиусом: {self.__radius():.2f}"

    def get_radius(self):
        return self.__radius()


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

        a, b, c = self.get_sides()
        s = (a + b + c) / 2  # находим полупериметр
        self.__height = 2 * math.sqrt(s * (s - a) * (s - b) * (s - c)) / a

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.__height



class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides, filled = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1] * self.sides_count


    def __str__(self):
        return f"Куб: {self.__sides}"

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

print('Проверка на изменение цветов')
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
#print(circle1.__str__())  # Вызов __str__
print(cube1.get_color())

print('Проверка на изменение сторон:')
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

print('Проверка периметра (круга), это и есть длина:')
# Проверка периметра (круга), это и есть длина:
print(len(circle1))

print('Проверка объёма (куба):')
# Проверка объёма (куба):
print(cube1.get_volume())
#*******************************************
print('Радиус круга:')
print(circle1.get_radius())

print('Площадь круга:')
print(circle1.get_square())

print('Строковое представление круга:')
print(circle1)
triangle1 = Triangle((202, 25, 13), 11, 8, 7)
print('Площадь треугольника:')
print(triangle1.get_square())
cube2 = Cube((222, 35, 130), 9, 3)
print(cube2)

