class Student:
    def __init__(self): #initialization
        self.name = "Rolf"
        self.grades = (10, 20, 30, 40)

    def __str__(self): #object used as string
        #return "Python Class"
        return f"person {self.name}"

    def __repr__(self): #Object used by programmers
        return f"<Student({self.name}), with grades ({self.grades})>"
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student()
print(student)
print(student.name)
print(student.grades[1])
#print(Student.average(student))
print(student.average())

class Teacher:
    def __init__(self, name):
        self.name = name
teacher = Teacher("John")
print(teacher.name)

class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")
    @staticmethod
    def static_method():
        print("Called static method")

ClassTest.static_method()
ClassTest.class_method()

test = ClassTest()
test.instance_method()


class Book:
    Types = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight} g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.Types[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.Types[1], page_weight - 100)

book = Book.hardcover("Namaste", 1000)
print(book)
book = Book.paperback("London",500)
print(book)
book = Book("Harry Potter", "comic", 1500)
print(book)