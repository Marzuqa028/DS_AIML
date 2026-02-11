# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:22:19 2026

@author: sumai
"""
import pandas as pd
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s1)
print(s2)

marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])
print(marks['Math'])
print(marks[['Math', 'Chemistry']])

scores = pd.Series([45, 67, 89, 34, 90])
passed = scores[scores > 60]
print(passed)

data = pd.Series([10, None, 30, None])
print(data.isnull())
print(data.fillna(9))

names = pd.Series(['Alice', 'bob', 'CHARLIE'])
print(names.str.lower())
print(names.str.contains('a'))

#task 1 The Product Catalog
products = pd.Series([700,150,300],index=['Laptop','Mouse','Keyboard'])
print("Laptop price: ",products['Laptop'])
print("First two producs\n",products[0:2])
print("Full Series\n",products)

#task 2 The Grade Filter
grades = pd.Series([85,None,92,45,None,78,55])
print("Original Series:\n",grades)
print(grades.isnull())
filled_grades = grades.fillna(0)
filtered = filled_grades[filled_grades>60]
print("Filled Series",filled_grades)
print("Grades greater than 60\n",filtered)

#task 3 The Username Formatter
usernames = pd.Series( [' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
usernames = usernames.str.strip()
cleaned = usernames.str.lower()
print(cleaned)
print(cleaned.str.contains('a'))

