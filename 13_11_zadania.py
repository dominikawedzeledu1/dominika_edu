# -*- coding: utf-8 -*-
"""13.11-zadania

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Ci0UGDTjCrRxaPgXS4fXrrrIVCdY6fp

Zad.1
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Dominika", [60, 80, 80])
student2 = Student("Ala", [70, 30, 20])

result1 = student1.is_passed()
result2 = student2.is_passed()

print(f"{student1.name} passed: {result1}")
print(f"{student2.name} passed: {result2}")

"""Zad.2"""

class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\nOpen hours: {self.open_hours}\nPhone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}, {self.city}, {self.street}, {self.zip_code}\nHire date: {self.hire_date}\nBirth date: {self.birth_date}\nPhone: {self.phone}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}, {self.publication_date}\nPages: {self.number_of_pages}\n{self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        book_list = "\n".join([f"  - {book}" for book in self.books])
        return f"Order by {self.employee.first_name} {self.employee.last_name} for {self.student.first_name} {self.student.last_name}\nOrder date: {self.order_date}\nBooks:{book_list}"



library1 = Library("City1", "Street1", "12345", "9:00 AM - 5:00 PM", "123-456-789")
library2 = Library("City2", "Street2", "54321", "10:00 AM - 6:00 PM", "987-654-321")

employee1 = Employee("Dora", "Mak", "2022-01-01", "1990-05-15", "City1", "Street1", "12345", "111-222-333")
employee2 = Employee("Dorota", "Lak", "2022-02-01", "1985-10-20", "City2", "Street2", "54321", "444-555-666")
employee3 = Employee("Dominika", "Wędzel", "2022-03-01", "1995-03-05", "City1", "Street1", "12345", "777-888-999")

book1 = Book(library1, "2021-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-02", "Author2", "Surname2", 300)
book3 = Book(library2, "2023-03-03", "Author3", "Surname3", 250)
book4 = Book(library2, "2020-04-04", "Author4", "Surname4", 180)
book5 = Book(library2, "2019-05-05", "Author5", "Surname5", 150)

student1 = Employee("Klaudia", "Fidyk", "2021-09-01", "2000-08-10", "City1", "Street1", "12345", "999-888-777")
student2 = Employee("Kostek", "Szmul", "2020-08-01", "1998-07-20", "City2", "Street2", "54321", "666-555-444")
student3 = Employee("Bartek", "Makel", "2023-04-01", "2002-02-15", "City1", "Street1", "12345", "333-222-111")

order1 = Order(employee1, student1, [book1, book2, book3], "2023-11-20")
order2 = Order(employee2, student2, [book4, book5], "2023-11-21")


print(order1)
print("\n")
print(order2)

"""Zad.3"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Property:\nArea: {self.area} sq. meters\nRooms: {self.rooms}\nPrice: ${self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House:\n{super().__str__()}\nPlot size: {self.plot} sq. meters"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat:\n{super().__str__()}\nFloor: {self.floor}"



house = House(area=150, rooms=4, price=25000, address="Maja 2", plot=300)
flat = Flat(area=80, rooms=3, price=250000, address="456 Avenue", floor=2)


print(house)
print("\n")
print(flat)