import math 

print(math.sqrt(25))
print(math.pow(2,3))


response_time = 81

result = math.sqrt(response_time)
print("result = ", result)


import random 

number = random.randint(1,100)
print(number)


number = random.randint(300,500)
print(number)

age = random.randint(18,60)
print("test age: ", age)


otp = random.randint(1000,9999)
print("generated otp: ", otp)


username = random.randint(1000,9999)
username = "tester" + str(number)
print(username)




import datetime

today = datetime.date.today()
print(today)


todays = datetime.date.today()
print(today)



from datetime import datetime
now = datetime.now()
print(now)



current = datetime.now()
print(current)


import os 
print(os.getcwd)

import os 
files = os.listdir 
print(files)



import os 

os.mkdir("screenshot")
print("folder created..")


if os.path.exists("screenshot"):
    print("folder exists")
else:
    print("folder does not exit")



import os 

folder = "screenshots"

if not os.path.exists(folder):
    os.mkdir(folder)

print("screensshot folder ready...")


import json
data = '{"name" : "chandan", "age" : 21 }'

result  = json.loads(data)

print(result)





