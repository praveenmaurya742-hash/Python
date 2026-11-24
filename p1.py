# Module 6 – Operators 
a = int(input("Enter the number ="))
b = int(input("Enter the number ="))
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b)
#🔹 2️⃣ Assignment Operators
a += 5
b -= 6
print(a)
print(b)
#🔹 3️⃣ Comparison Operators
print(10 == 10)
print(10 > 5)
print(5 < 10)
print(10 != 5)
#🔹 4️⃣ Logical Operators
age =20
print(age >18 and age < 30)
# 🔹 5️⃣ Membership Operators
fruits = ["apple", "banana","mango"]
print("apple" in fruits)
print("grapes" not in fruits)
# combined Example
age = 22
if age > 18 and age < 30:
    print("Eligible")
else:
    print("Not Eligible")
#🔹 Practice Programs
# 1 even / odd
num= int(input("Enter number:"))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# Simple calculator
a  = 10
b = 5
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
# 3. check name in list
students = ["Rahul" in students]
print("Rahul" in students)
print("Riya" not in students)
# 4 Greater number
a = 20 
b = 16
print(a>b)


