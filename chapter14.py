"""
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()

class Rectangle:
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)
print(Rectangle.recs)


class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)



class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)


print(x + y)
"""

"""
class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

print(same_bob)
print(bob)
print(another_bob)
"""

"""
x = 10
if x is None:
    print("x はNone :( ")
else:
    print("x はNoneじゃない")

x = None
if x is None:
    print("x はNone")
else:
    print("x はNoneじゃない :( ")
"""

# Challenge1
"""
class Square:
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

a_square = Square(5)
print(a_square.square_list)

b_square = Square(6)
print(a_square.square_list)
"""

"""
# Challenge2
class Square:
    square_list = []

    def __init__(self, s):
        self.side = s

    def print_side(self):
        print("{} by {} by {} by {}".format(self.side, self.side, self.side, self.side))

a_square = Square(5)
print(a_square.print_side())
"""

"""
# Challenge3
def two_argument(a1, a2):
    if a1 is a2:
        print(a1 is a2)
    else:
        print(a1 is a2)

two_argument(4, 4)
"""

"""
class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)

a_square = Square(29)
print(a_square)

"""

def compare(obj1, obj2):
    return obj1 is obj2

print(compare("a", "b"))
print(compare("a", "a"))
