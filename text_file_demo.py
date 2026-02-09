file = open("sample.txt","w")
file.write("Hello, this is a file handling example.")
file.close()
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()


with open("sample.txt", "r") as file:
    content = file.read()
    print(content)



try:
    with open("missing.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found. Please check the filename.")

import csv
with open("data.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0:2])


with open("data.xlsx","r")as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

import pandas as pd
data = pd.read_excel("data.xlsx")
print(data)


#task 1 the personal logger
name = input("Enter your name ")
daily_goal = input("Enter your daily goal:")
with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Goal:{daily_goal}\n")

#task 2 The CSV Student List
import csv
with open("students.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[2] == "Pass":
            print(row[0])


#task 3 The Safe Opener
filename = input("Enter a file name: ")
try:
    with open(filename,"r") as f:
        print(f.read())
except FileNotFoundError:
    print("Oops! That file doesn't exist yet")