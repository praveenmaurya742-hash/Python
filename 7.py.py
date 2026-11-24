#list creatioon
num=[1,2,3]
students =["Amit","Rahul","Neha"]
#list indexing
print(num)
print(students)
nums =[1,2,3]
print(nums[0])
print(nums[2])

#tuple creation
t1=(1,2,3)
t2=1,2,3
print(t1)
print(t2)
#tuple features
data=(10,"Python",'true')
print(data)
#tuple methods( Only 2 methods)
t=(10,20,30,20)
print(t.count(20))
print(t.index(30))
#tuple unpacking
data1=(10,20)
a,b= data1
print(a)
print(b)
#multiple example
student=("Rahul",21,"Bhopal")
name,age,city = student
print(name)
print(age)
print(city)
#list
items = ["milk","bread"]
items.append("butter")

#tuple
coordinates = (23.45,77.41)


#complete class Example
student = ("Rahul",21, "Bhopal")
name, age, city= student
print(f"Name:{name}")
print(f"age:{age}")
print(f"city:{city}")