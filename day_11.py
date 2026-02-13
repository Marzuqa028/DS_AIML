# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 10:14:01 2026

@author: sumai
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 11]
plt.plot(x, y)
plt.show()


x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
plt.scatter(x, y)
plt.show()


categories = ['A', 'B', 'C']
values = [11, 20, 15]
plt.bar(categories, values)
plt.show()

plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9])
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()

import matplotlib.pyplot as plt
plt.subplot(1, 2, 1)
plt.plot([1,2,3], [1,4,9], label="y = x^2")
plt.plot([1,2,3], [1,2,3], label="y = x")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line Plot")
plt.subplot(1, 2, 2)
plt.bar(['A','B','C'], [3,7,5])
plt.title("Bar Chart")
plt.show()


#task : the trend tracker
import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]
plt.plot(months,revenue) 
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")
