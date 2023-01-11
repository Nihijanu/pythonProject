# def add(x,y):
#    return x+y
# a=add
#  print(a(10,20))
def inc(x):
    return x+1
def dec(x):
    return x-1
def operator(func,n):
    r=func(n)
    return r
print(operator(dec,10))

n1=int(input("enter number:"))
n2=int(input("enter number:"))
def even():
    for i in range(n1,n2):
        if i%2==0:
            print(i)
def odd():
    for i in range(n1,n2):
        if i%2!=0:
            print(i)
def operator1(func):
    func()
operator1(even)
operator1(odd)
