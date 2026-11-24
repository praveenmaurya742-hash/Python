#1️⃣ Dictionary Creation
student={"name":"Amit","Age":20}
print(student)
# dictionary features
data ={"name":"Amit","course":"Python","Active":True}
print(data)
#2️⃣ Value Access using Key
student = {"name":"Amit","age":20}
print(student["name"])
print(student["age"])
# Safe Access using get()
student = {"name0":"Amit","age":20}
print(student.get("city"))
#🔹 keys() Method
student ={"name":"Amit","age":20}
print(student.keys())
#🔹 values() Method
student = {"name":"Amit","age":20}
print(student.values())
#🔹 items() Method
student ={"name":"Amit","age":20}
print(student.items())
#loop with Dictionary
student = {"name": "Amit", "age": 20}
for key, value in student.items():
    print(key, "=", value)
# Add/ Update Dictionary Data
student = {"name":"Amit","Age":21}
student["City"]="Bhopal"
print(student)
#🔹 Update existing value
student ={"name":"Amit","age":20}
student["age"]=21
print(student)
#🔹 update() Method
student = {"name":"Rahul","Age":20}
student.update({"age":21,"City":"Bhopal"})
print(student)
#🔹 setdefault() Method
student= {"name":"Rahul","age":20}
print(student.setdefault("city","Bhopal"))
print(student)
#🔹 pop() Method
#💻 Example
student = {"name": "Rahul", "age": 20, "course": "Python"}
removed = student.pop("course")
print(removed)
print(student)
#🔹 popitem() Method
#💻 Example
student = {"name": "Rahul", "age": 20, "course": "Python"}
print(student.popitem())
print(student)
#🔹 clear() Method
#💻 Example
student = {"name": "Rahul", "age": 20}
student.clear()
print(student)
#🔹 del Keyword
#💻 Example
student ={"name":"Rahul","age":20,"city":"Bhopal"}
del student["age"]
print(student)
#🔹 copy() Method
#💻 Example 
student = {"name": "Rahul", "age": 20}
new_student = student.copy()
print(new_student)
#🔹 fromkeys() Method
#💻 Example
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Not Given")
print(new_dict)
#🔹 Dictionary vs List
students = ["Amit", "Rahul", "Neha"]
student = {"name": "Amit", "age": 20}
print(student)
print(students)
#complete Combined example
student = {
    "name":"Rahul",
    "Age":20,
    "course":"Python"
}
print(student.get("name"))
student["city"]="Bhopal"
student.update({"age":21})
student.pop("course")
for key, value in student.items():
    print(key,"=",value)

