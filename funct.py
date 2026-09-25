def greet(name):
    print("hello",name)

greet("chandan")


def add(a,b):
    print(a + b)

add(10,20)



def students(name, age):
    print(name, age)

students("chandan", 20)

def test(name = "tester"):
    print("hello", name)

test()


def adds(*numbers):
    print(numbers)


adds(10,20,30,40,50)



def argss(*args):
    print(args)


argss(12,34,45,567)


def kwargss(**kwargs):
    print(kwargs)

kwargss(name = "chandan" , age = 12, college = "techspire")



def fuct(a,b):
    return a + b

result = fuct(10,20)
print(result)

print(fuct(12,12))

#nested function

def outer(x):
    def inner():
        print(x)
    return inner
func = outer(10)
func ()

#function with no para 
def message():
    print("hello")

message()

def student_info(name, age, course):
    print("name", name)
    print("age", age)
    print("course", course)

def add(a,b):
    return a + b

result = add(10,20)
print("result = ", result)



def add(a,b):
    return a + b

def show_result():
    result = add(10,20)
    print(result)

show_result()



