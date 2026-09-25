# def login():
#     print("opening login page")
#     print("Entering username")
#     print("entering password")
#     print("clicking login button")



# login()



# #build in function
# user_name = "chandan"
# print(len(user_name))


# password = "abc12345"
# if len(password) >= 8:
#     print("password length valid")
# else:
#     print("password length invalid")


# status_code = 200
# print(type(status_code))


# code = 400
# message = "status code:  " + str(code)
# print(message)

# response_times = [120,23,45,67,89,90]
# print(max(response_times))
# print(min(response_times))


# total = sum(response_times)
# print(total)

# sort = sorted(response_times)
# print(sort)


# for i in range(5):
#     print(i)


# for i in range(3):
#     print("Running test", i + 1)



# def get_status_code():
#     status_code = 200 
#     return status_code

# status = get_status_code()

# if status == 200:
#     print("API test passed")
# else:
#     print("API test failed")



# def login(username, password):
#     print(username)
#     print(password)

# login(password = "admin@123", username = "chandan sah")


# def verify_status(status_code):
#     if status_code == 200:
#         return "Pass"
#     else:
#         return "Fail"

# result = verify_status(200)
# print(result)



# def run_login_tests(users):
#     for user in users:
#         print("Testing user: " , user)

# users = ["admin" , "tester" , "guest"]
# run_login_tests(users)


def verify_user(user):
    print("name :", user["name"])
    print("Role : ", user["role"])

    user = {
        "name": "chandan",
        "role": "QA"

    }

    verify_user(user)


def verify_status_code(actual, expected):
    if actual == expected:
        return True

    else:
        return False


result = verify_status_code(200,200)
print(result)


print(result)


def open_browser():
    print("Browser Opened")


def login():
    open_browser()
    print("login performed")


def verify_dashboard():
    login()
    print("Dashboard verified")

verify_dashboard()


#practical mini automation program 
def open_browser():
    print("Browser opened")

def login(username, password):
    print("username: ", username)
    print("password : " , password)
    print("Login clicked")


def get_status_code():
    return 200

def verify_status_code(actual,expected):
    if actual == expected:
        return True
    else:
        return False

def close_browser():
    print("browser closed..")


open_browser()
login("admin", "admin123")
status = get_status_code()
result = verify_status_code(status, 200)

if result:
    print("login test passed..")
else:
    print("login test failed..")

close_browser()


# LIS = []
# TUPE = ()
# Dictionary = {key:value}
# set = {}


text = "Python"
print(len(text))



number = 10.567
print(round(number))


print(abs(-10))
