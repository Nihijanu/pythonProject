from datetime import datetime
def get(func):
    def wrapper():
        print("function name:",func.__name__)
        print(datetime.today().strftime("%y-%m-%d %H:%M:%S:%MS"))
        func()
    return wrapper
@get
def login():
    print("i am login in function")
login()
@get
def logout():
    print("i am logout function")
logout()

