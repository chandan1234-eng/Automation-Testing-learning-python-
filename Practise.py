#type conversion

age = 20
age = str(age)

print(age)
print(type(age))

#f string 
name = "chandan"
age = 20

print(f"my namne is {name} and age is {age}")


a = 10
b = 20

print(f"sum is: {a+b}")


marks = 30

if age >= 18:
    print("adult")


color = "red"

if color == "red":
    print("go..")
elif color == "green":
    print("B")


if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("fail")



# nested conditions
Age = 20
has_id = True

if Age >= 18:
    if has_id:
        print("Entry allowed")


#for loops 


for i in range(5):
    print("hello")


Fruits = ["apple", "baanan" , "mango"]

for i in Fruits:
    print(i)




#while loops 
# count  = 1
# while count <= 5:
#     print(count)

# count  += 1 



#break 

for i in range(10):
    if  i == 5:
        print(i)
        break
    print(i)



#continue 
for i in range(5):
     if i == 2:
         continue
     print(i)



for i in range(0,10,2):
    print(i)

names = ["Ram", "sita", "Hari"]
ages = [20, 22, 19]
for name, ages in zip(names, ages):
    print(name, age)


numbers  = [1,3,5,8]
result = any(n%2 == 0 for n in numbers)
print(result)


num1  = [1,3,5,8]
result = all(n%2 == 0 for n in num1)
print(result)









    

 