#task 1 The Area & Perimeter 
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2*(length + width)
    return area, perimeter
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
result = calc_rectangle(length,width)
print("The area and the perimeter of the rectangle is ", result)


#Task 2 The Logic Library 
import math_operations
power = math_operations.power(2,10)
print("2 to the power of 10 is: ",power)
list = [10,20,30,40]
average = math_operations.average(list)
print("the average of [10,20,30,40] is: ", average)

def greet():
    print("Hello, welcome to the internship")
greet()


def add_numbers(a,b):
    return a+b
result = add_numbers(5,3)
print(result)

x = 10
def show_value():
    x = 5
    print(x)
print(x)
show_value()


icecream = "vanilla"
def food():
    fruit = "mango"
    vegetable = "cucumber"
    print(fruit, "is good for health")
    print(icecream,"is good for health")
food()
print(vegetable,"is good for health")

import random

print(random.randint(1, 10))
print(random.randint(1, 10))

import random

random.seed(10)

print(random.randint(1, 100))
print(random.randint(1, 10))

