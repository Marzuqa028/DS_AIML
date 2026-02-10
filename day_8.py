# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])
c = np.array([[[1,2],[2,3]],[[5,7],[4,8]]])
d = np.array(4)
print(d)
print(a)
print(b)
print(c)
result = a+b
print(result)

arr = np.random.randint(1,100)
squared = arr**2

arr = np.arange(12)
reshaped = arr.reshape(3,4)
print(reshaped)
a = np.array([[1,2]])
b = np.array([[3,4]])
vstacked = np.vstack((a,b))
print(vstacked)
hstacked = np.hstack((a,b))
print(hstacked)

data = np.array([[10,20,30],[40,50,60]])
print(np.mean(data))
print(np.mean(data, axis = 0))
print(np.mean(data, axis = 1))

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))

arr = np.arange(0,12,2)
print(arr)
arr3d = arr.reshape(1,2,3)
print(arr3d)

arr = np.linspace(0,4,5)
print(arr)

arr = np.random.rand(2,2)
print(arr)

arr = np.array([1.2,2.8,-3.7])
print(np.floor(arr))
print(np.ceil(arr))
print(np.trunc(arr))
print(np.round(arr))


#task 1 The Normalizer
arr = np.random.randint(50,101,size = (5,3))
mean = np.mean(arr,axis = 0)
print(mean)
centered = np.add(arr,-mean)
print(f"Original array: {arr}\ncentered array: {centered}")


#task 2 The Reshaper
arr = np.arange(24)
print("Original 1D array", arr)
arr_1 = arr.reshape(4,3,2)
print("Reshaped array: ",arr_1)
arr_2 = arr_1.transpose(0,2,1)
print("Final transposed array and shape")
print(arr_2.shape)
print(arr_2)
