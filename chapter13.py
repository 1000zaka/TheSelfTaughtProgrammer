"""
class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)


data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)
"""

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # client が使っても良い
        pass # pass文は、文が必須な構文で何もしない場合に使う

    def _unsafe_method(self):
        # clientは使うべきではない
        pass # pass文は、文が必須な構文で何もしない場合に使う


"""
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

a_square = Square(20, 20)
a_square.print_size()
"""

"""
class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)
"""


# Challenge 1
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def caluculate_permeter(self):
        return self.length * self.width

class Square:
    def __init__(self, radius):
        self.radius = radius

    def caluculate_permeter(self):
        import math
        return self.radius ** 2 // math.pi

rectangle = Rectangle(6, 7)
print(rectangle.caluculate_permeter())
square = Square(7)
print(square.caluculate_permeter())
"""

# Challenge 2
"""
class Rectangle:
    def __init__(self):
        self.length = 5
        self.width = 6

    def change_size(self, length_plus, width_minus):
        self.length_plus = self.length - length_plus
        self.width_minus = self.width - width_minus


    def caluculate_permeter(self):
        return self.length_plus * self.width_minus

rectangle = Rectangle()
rectangle = rectangle.change_size(1, 1)
print(rectangle.caluculate_permeter())

class Square():
    def __init__(self, s1):
        self.s1 = s1

    def caluculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_square = Square(100)
print(a_square.s1)

a_square.change_size(200)
print(a_square.s1)
"""

"""
# Challenge3
class Shape:
    def what_am_i(self):
        print("I am a shape")

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def caluculate_perimeter(self):
        return self.s1 * 4

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def caluculate_permeter(self):
        return self.length * self.width

square = Square(5)
rectangle = Rectangle(5,3)

square.what_am_i()
rectangle.what_am_i()
"""

# Challenge 4
class Horse:
    def __init__(self, name):
        self.name = name

class Rider:
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

horse_nick_name = Horse("deep inpact")
rider = Rider("Masaki Katsuura", horse_nick_name)
print(rider.horse.name)

