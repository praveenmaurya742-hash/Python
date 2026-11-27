# 🔹 MODULE 9 – STRINGS
#🔹 1️⃣ STRING BASICS (DETAIL TABLE)
name = "Python"
city ="Bhopal"
print(name)
print(city)
#🔹 2️⃣ STRING INDEXING
name = "Python"
print(name[0])
print(name[3])
print(name[5])
#🔹 NEGATIVE INDEXING
name = "Python"
print(name[-5])
#🔹 3️⃣ STRING SLICING
name ="Python"
print(name[0:5])
#🔹 4️⃣ STRING METHODS
text ="hello Praveen"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())
#🔹 2. Searching Methods
text = "hello praveen"

print(text.find("p"))
print(text.count("o"))
print(text.startswith("h"))
print(text.endswith("n"))

#🔹 3. Modify Methods
text = "hello praveen"
print(text.strip())
print(text.replace("praveen","Maurya ji"))
#🔹 4. Split & Join 
text = " I love Python"
word = text.split()
print(word)

new_text = "-".join(word)
print(new_text)
#🔹 5. Check Methods (True/False)
text = "Python123"
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())

#🔹 5️⃣ f-STRING (MODERN WAY)
name = "Python"
print(f"Hello {name}")

name = "Rahul"
age = 25
print(f"My name is {name} and I am {age} years old")

a = 10
b = 20
print(f"Sum is {a+b}")
# 🔥 FINAL CLASS DEMO (BEST FOR STUDENTS)
name = "Praveen"
text = "hello python"

print(f"Hello {name}")
print(text.upper())
print(text.strip())
print(text.replace("python","java"))
print(text.strip())
