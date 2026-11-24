# set creation
s = {1,2,3}
print(s)
#set features
data ={10,"Python","true"}
print(data)
#list vs  set
nums =[1,2,3]
unique = set(nums)
print(unique)
# 4 unique values
nums = [1,2,3,4,4]
unique_nums=set(nums)
print ( unique_nums)
# set Methods- Complete table
#1. ADD / UPDATE METHODS
s = {1,2}
s.add(3)
print(s)
s.update([4,5])
print(s)
# 2. REMOVE METHODS
s = {1,2,3}
s.remove(2)
print(s)
s.discard(5)
print(s)
#pop() exapmle
s = {10,20,30}
item= s.pop()
print("Removes:",item)
print("Remaining:",s)
#clear() Example
s = {1,2,3}
s.clear()
print(s)
# 3. SET OPERATIONS (VERY IMPORTANT 🔥)
a = {1,2,3}
b = {3,4,5}
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
# 4. CHECK METHODS
a = {1,2}
b = {1,2,3}
c = { 4,5}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))
#REAL-LIFE STUDENT EXAMPLE
python_students = {"Rahul","Amit","Neha"}
java_students = {"Amit","Riya","Neha"}

print("Common Students:",python_students.intersection(java_students))
# IMPORTANT CONCEPTS
# 1. Duplicate remove automatically
s = {1,1,2,2,3}
print(s)
#2. Order fixed nahi hota
s = {3, 1, 2}
print(s)
# 3. No Indexing
s = {10, 20, 30}
print(s[0])
