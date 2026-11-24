#string basics
name = "Python"
city = "Bhopal"
print(name)
print(city)
# string indexing
name = "Python"
print(name[0])
print(name[3])
# negative indexing
name = "Python"
print(name[-1])
#string slicing (string[stat:end])
Name = "python"
print(name[0:4])
# string Methods
#case methods
text = "Hello world"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())
#searching Methods
text = "hello python"
print(text.find("p"))
print(text.count("o"))
print(text.startswith("h"))
print(text.endswith("n"))
#modify methods
text = "hello python"
print(text.strip())
print(text.replace("python","java"))
#split & join
text ="I Love python"
words = text.split()
print(words)
new_text = " ".join(words)
print(new_text)
#chech Methods
text ="Python123"
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())
#f-string (modern way)
name = "Praveen"
print(f"Hello {name}")
name = "Rahul"
age = 25
print(f"My name is {name} and I am {age} years old")
a = 10
b = 20
print(f"Sum is {a + b}")
#finial class demo
name = "Rahul"
text = "hello Python"
print(f"Hello {name}")
print(text.upper())
print(text.strip())
print(text.replace("python","java"))
print(text.split())
