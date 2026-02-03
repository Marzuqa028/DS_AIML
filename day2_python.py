
age = 21
print(type(age))
height = 5.8
print(type(height))
name = "shreyas"
print(type(name))
is_student = True
print(type(is_student))

#Simple Calculator
print("Simple Calculator")

choice = input("Enter choice (+/-/*//): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "+":
    print("Result:", num1 + num2)

elif choice == "-":
    print("Result:", num1 - num2)

elif choice == "*":
    print("Result:", num1 * num2)

elif choice == "/":
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid choice")

#concatenation
name = input("Enter your name: ")
print("Welcome",name,"!")
print("Welcome "+name +"!")
print(f"Welcome {name}!")

#typecasting
b = 5.2
print(complex(b))

#task1
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Age in 2030 = {int(age) + 4}")


#task 2 : The bill Splitter
total = float(input("Enter the total bill amount: "))
noofppl = int(input("Enter the total no.of people: "))
share = total/noofppl
print(f"Total Bill: {total}. Each person pays: {share}")


#task 3 : The Raw Data Formatter
item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True
print(f"Item : {item_name}, Qty : {quantity}, Price: {price}, Available:{in_stock}")
total_cost = quantity * price
print(f"Total cost: {total_cost}")
