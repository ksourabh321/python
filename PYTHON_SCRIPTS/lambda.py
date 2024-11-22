# Normal function def and execution
def doubler(n):
  return n*2

doubler(10)
  
x=doubler(10)
print(x)

--------------------------------------------
# Assignment of function to a variable

x=doubler
print(x(10))

---------------------------------------------
# Assignment of lambda function to a variable

x=lambda a : a*2
print(x(10))

x=lambda a , b : a*b
print(x(10,2))

x=(lambda a , b : a*b)(10,2)
print(x)

print((lambda a , b : a*b)(10,2))
---------------------------------------------

def myfunc(n):
  return lambda z : n*z

x=myfunc(2)----doubler object/instance
print(x(10))

y=myfunc(3)----tripler object/instance
print(y(10))

-----------------------------------------------
def doubler(n):
  return n*2
  
def tripler(n):
  return n*3

x=doubler
def myfunc(n,x):
    return x(n)
    
x=tripler
def myfunc(n,x):
    return x(n)