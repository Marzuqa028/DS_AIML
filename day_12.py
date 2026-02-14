# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:44:00 2026

@author: sumai
"""
#Task 1 Correlation Checker
import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8] 
scores = [50, 55, 65, 70, 75, 85, 90, 95]
plt.scatter(study_hours,scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.show()

#Task 2 The Comparison Dashboard
import matplotlib.pyplot as plt
plt.subplot(1, 2, 1) 
categories = ['Electronics','Clothing','Home']
values = [300,450,200]
plt.bar(categories,values)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")
plt.subplot(1,2,2)
plt.plot([1, 2, 3, 4, 5],[2, 4, 6, 8, 11])
plt.title("Sales Trend Over Time")
plt.xlabel("Time")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

