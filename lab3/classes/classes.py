# Task 1:
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Write string: ")
        
    def printString(self):
        print(self.string.upper())

# Print Task 1:
manipulator = StringManipulator()
manipulator.getString()
manipulator.printString()

# Task 2:
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# Print Task 2:
square = Square(5)
print("Area of square:", square.area())

# Task 3:
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length * self.width

# Print Task 3:
length=float(input("length: "))
width=float(input("width: "))
rectangle=Rectangle(length, width)
print("Area of rectangle:", rectangle.area())

# Task 4:
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"coordinates {self.x},({self.y})")

    def move(self, dx,dy):
        self.x+=dx
        self.y+=dy

    def dist(self, general):
        return ((self.x-general.x)**2 + (self.y-general.y)**2)**0.5

# Print Task 4:
point1 = Point(2,3)
point1.show()

# Task 5:
class bank_cash:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,sum):
        self.balance += sum
        print(f"Принят депозит в размере данной суммы: {sum}")

    def withdraw(self,sum):
        if sum <=self.balance:
            self.balance -= sum
            print(f"Снятие {sum} принято!")
        else:
            print("Недостаточно средств!")

# Print Task 5:
account = bank_cash("John", 1000)
account.deposit(500)
account.withdraw(2000)

# Task 6:
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Print Task 6:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)

