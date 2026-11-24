#Arithmetic Operators
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
#Assignment Operators
x = 10
x += 5
print(x)
#Comparison Operators
print(10 == 10)
print(10 > 5)
print(5 < 10)
print(10 != 5)
# logical Operators
age = 20
print(age > 18 and age < 30)
age = 70
print(age < 18 or age > 60)
print(not True)
print(not False)
# Membership Operators
frutis = ["apple","banana","mongo"]
print("apple" in frutis)
print("grapes" not in frutis)
# combined Example
age1 = 22
if age1 > 18 and age1 < 30:
    print("Eligible")
else:
    print("Not Eligible")
# Practice Progrms
# 1. Even / Odd
num = int(input("Enter number: "))
if num %2 == 0:
    print("Even nnumber")
else:
    print("Odd number")
#2. simple calculator
a = 10 
b = 4
print("add:", a + b)
print("subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)
#3.check name i list
students =["Rahul", "Amit", "Neha"]
print("Rahul" in students)
print("Riya" not in students)
# 4. Greater Number
a = 20
b = 15
print (a > b)

c =int(input("Enter the first Number: "))
d =int(input("Enter the Second number:"))
print("Sum=", c+d)
print("Subtract", c-d)
print("Multipl", c*d)
print("Divison", c/d)