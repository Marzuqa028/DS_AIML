"""
numbers = [10,20,30,40]
coordinates = (5, 10)
print(numbers)
print(coordinates)

a = [100,200,300,400,500,600,700,800]
print(a[6])
print(a[-6])
print(a[0:8:3])
print(a[-7:-1:2])


marks = [32,62,387,25,28,436]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)


#task 1 Inventory manager
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print(inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print(inventory)


#task 2 The data Slicer
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First temp: ", temperatures[0])
print("Last temp: ",temperatures[-1])
print("Afternoon Peak Readings", temperatures[3:6])
print("Last 3 hours", temperatures[-3:])
"""

#task 3 The Immutable Config
screen_res = (1920, 1080)
print(f"Current Resolution: {screen_res[0]}x{screen_res[1]}")
#screen_res[0] = 1280
print("Tuples cannot be modified!")