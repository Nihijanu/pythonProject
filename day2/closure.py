def fun1(txt):
    def fun2():
        print(txt)
    def fun3():
        print("hi")
    return fun2,fun3
msg,msg2=fun1("hello")
msg()
msg2()


'''def add_num(n):
    def add(x):
        return x+n
    return add
z=add_num(10)
y=add_num(12)
print(z(5))
print(y(3))'''

def func1(fun):
    def func2():
        print("hello from func 2")
        fun()
    return func2
@func1
def demo():
    print("hi how r u")
#f=func1(demo)
#f()
demo()