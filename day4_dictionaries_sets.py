
"""
a = {"age":21,"name":"sumi"}
print(a)
student = {"name":"Sumi","age":21, "course":"Engineering"}
print(student)
print(student["name"])
student["age"]=22
student["city"]="Delhi"
print(student)
print(student.get("place"))
for key,value in student.items():
    print(key,value)

marks = {"math":80,"science":75,"english":85}
print(marks.get("math"))
print(marks.get("history",0))
for key,value in marks.items():
    print(key,value)
marks.update({"python":90})
print(marks)


purchases = {"Alice":250,"Bob":400,"Charlie":150}
for name,amount in purchases.items():
    print(f"{name} spent ₹{amount}")
print("Total customers:",len(purchases))
print("Customer Names:",purchases.keys())
print("Customer amounts:",purchases.values())

n = int(input("Enter the no.of customers"))
user_purchases = {}
for i in range(n):
    name = input("Enter customer name: ")
    amount = int(input(f"Enter purchase amount for {name}:"))
    user_purchases[name]=amount
print("Customer Purchase Data:",user_purchases)

top_customer=max(purchases,key=purchases.get)
print("top Spending customer:", top_customer)
least_customer=min(purchases,key=purchases.get)
print("Least Spending customer:", least_customer)
purchases.update({"David":500})


#task 1 The personal contact book
contacts = {"sumi":"3275","haya":"3947","ezlin":"73125"}
contacts.update({"chachu":"377777777734"})
contacts.update({"sumi":"123456789"})
print("Contact details of sumi: ", contacts.get("sumi"))
print("Contact details of rufi: ", contacts.get("rufi","Contact not found"))
print("All Contacts: ")
for contact,phone in contacts.items():
    print(f"Contact:{contact},Phone:{phone}")


#task 2 The Duplicate Cleaner
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
print("ID05" in unique_users)
print(f"The length of the original list:{len(raw_logs)} and the length of the unique set:{len(unique_users)}")
"""

#task 3 The interest Matcher
friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(f"Common Interests:{friend_a & friend_b}")
print(f"All Interests:{friend_a | friend_b}")
print(f"Interests that friend_a has but friend_b doesnt: {friend_a - friend_b}")
