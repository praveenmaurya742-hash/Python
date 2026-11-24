# for loop
for i in range(1,6):
    print(i)
# range()
for i in range(5):
    print(i)
for i in range(2,10,2):
    print(i)
# while loop
i = 1
while i <=5:
    print(i)
    i +=1
# break
for i in range(1,10):
    if i == 5:
        break
    print(i)

# countine 
for i in range(1,6):
    if i == 3:
        continue
    print(i)
    
# pass
for i in range(1,6):
    if i == 3:
        pass
    print(i)

#break vs continue vs pass
for i in range(1,12):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)
# for loop
for i in range(1,4):
    print(i)
# while loop
i = 1
while i <=3:
    i +=2
# table print 
num =int(input("Enter number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
# sum of number
total = 0
for i in range(1,6):
    total +=1
    print("Total:", total )
# while loop ex
i = 1
while i <=5:
    print("Hello")
    i +=1
# even number
for i in range(2,11,2):
    print(i)
#skip One number
for i in range(1,6):
    if i == 4:
        continue
    print(i)
    