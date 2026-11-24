# if statement
age = 19
if age >= 18:
    print("Adult")

marks = 90
if marks >=40:
    print("Pass")
#if-else Statement
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

num = 5
if num %2 == 0:
    print("Even")
else:
    print("Odd")

#elif Statement
age = 65
if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

marks = 75
if marks >=90:
    print("Grade A")
elif marks >=60:
    print("Grade B")
elif marks >=40:
    print("Pass")
else:
    print("Fail")

# only if
age = 20
if age >= 18:
    print("adult")
# if-else
age =15
if age >= 18:
    print("Adult")
else:
    print("Minor")
# if-elif-else
marks = 35
if marks >= 90:
    print("Grade A")
elif marks >=40:
    print("Pass")
else:
    print("Fail")
#combined Exa
marks = 75
if marks>= 90:
    print("Grade A")
elif marks >=60:
    print("Grade B")
elif marks >=40:
    print("Pass")
else:
    print("Fail")
# Nested if Extra Concept
age = 20
has_id = True
if age >= 18:
    if has_id == True:
        print("Entry Allowed")

age = 18
if age == 18:
    print("Exactly 18")

# practice Programe
# even / Odd
num = int(input("Enter number1:"))
if num %2 == 0:
    print("Even")
else:
    print("Odd")
# Positive / Negative / Zero
num =int(input("Enter number:"))
if num >0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")
#login check
username = input("Enter username:")
if username == "admin":
    print("Login Success")
else:
    print("Access Denied")

#largest of two number
a = 10
b = 20
if a > b:
    print("A is greater")
else:
    print("B is greater")

#Grade System
marks = 88
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >=40:
    print("Pass")
else:
    print("Fail")

name = input("Enter Name:")
if name =="":
    print("Please Enter Your?")
else:
    print("You are name:",name)