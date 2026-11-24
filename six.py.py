#list creation
nums = [1,2,3]
students = ["Amit", "Rahul","Neha"]
print(nums)
print(students)
print(students[1])
#list indexing
nums = [1,2,3]
print(nums[0])
print(nums[2])
#complete combined
numbers = [10,20,30]
numbers.append(40)
numbers.insert(1,15)
numbers.remove(20)
numbers.sort()
print(numbers)
#real-life example
students =[]
students.append("Rahul")
students.append("Amit")
students.append("Neha")
print(students)
#list mutable hoti hai
a = [1,2,3]
a[0] = 10
print(a)
#append() vs extend()
a= [1,2]
a.append([3,4])
print(a)
a = [1,2]
a.extend([3,4])
print(a)
# tuple creation
t1 = (1,2,3)
t2 = (4,5,6)
print(t1)
print(t2)
#single vatue tuple
t = (5,)
print(t)
#tuple features
data = (10,"Python",True)
print(data)
#tuple indexing
t = (10,20,30)
print(t[0])
print(t[-1])

# tuple methods
# count() & index ()
t = (10,20,30,20)
print(t.count(20))
print(t.index(30))
#tuple unpacking
data = (10,20)
a,b = data
print(a)
print(b)
#multiple example
student = ("Rahul", 21, "Bhopal")
name, age, city = student
print(name)
print(age)
print(city)
# tuple vs list (very important)
#list 
items = ["milk","bread"]
items.append("butter")

#tuple 
coordinates = (23.45,77.41)
# complete class example
student = ("Rahul",21,"Bhopal")
name, age,city = student
print(f"Name:{name}")
print(f"Age:{age}")
print(f"City:{city}")
