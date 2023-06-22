import math


def motto():
    print("This is our motto")


motto()


def vision():
    print("This is our vision")


vision()
motto()
vision()
motto()


def add():
    x = 10
    y = 20
    z = x + y
    print(z)


add()
add()
add()


def avg(x, y, z):
    average = (x + y + z)/3
    print("Your average is " + str(average))


avg(40, 60, 30)
avg(50, 200, 300)


def bmicalc(weight, height):
    bmi = weight / pow(height, 2)
    if bmi <= 18:
        print("Underweight")
    elif bmi <= 29:
        print("Normal Weight")
    elif bmi <= 34:
        print("Overweight")
    else:
        print("Obese")


bmicalc(118, 60)


def grade(marks):
    if marks < 40:
        print("E")
    elif marks < 50:
        print("D")
    elif marks < 60:
        print("C")
    elif marks < 70:
        print("B")
    else:
        print("A")


grade(76)
grade(20)
grade(59)


def login(email, password):
    if email == "user@example.com" and password == "user123":
        grade(90)
    else:
        print("Login failed")


login("user@example.com", "user123")


def areaofacircle(radius):
    area = math.pi * pow(radius, 2)
    return area


print(areaofacircle(7))
