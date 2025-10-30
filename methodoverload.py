from multipledispatch import dispatch
@dispatch(int, int)
def product(a,b):
    print("Result : ", a*b)

@dispatch(int, int, int)
def product(a,b,c):
    print("Result :", a*b*c)

@dispatch(int, int, int, int)
def product(a,b,c,d):
    print("Result :", a*b*c*d)
    
product(2,3)
product(2,3,4,5)
product(2,3,4)
product(2,3)