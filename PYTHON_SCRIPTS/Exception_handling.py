#PYTHOON EXCEPTION HANDLING
 
#Example of exception in block code:

x='example'
print(x+5)

----------------------------------------
#Example of exception in Function:

def myfunc(x):
    x=x+5
    print(x)

myfunc('example')

----------------------------------------
#Handling of Exception in block code

x='example'
try:
    print(x+5)
except:
    print('cant add number to string')
    
-----------------------------------------
#Handling of Exception in Function

def myfunc(x):
    try:
        x=x+5
        print(x)
    except:
        print('cant add number to string')
    
myfunc('example')

--------------------------------------------------------------
#Exception handling with printing exception error name and msg

def myfunc(x):
    try:
        x=x+5
        print(x)
    except Exception as ex:
        print('cant add number to string')
        print(type(ex).__name__)
        print(ex)
    
myfunc('example')

---------------------------------------------------------------
#Exception handling with mutiple exceptions
def myfunc(x):
    try:
        x=x/0
        print(x)
    except TypeError:
        print('cant add number to string')
    except Exception as ex:
        print('There might be some other error')
        print(type(ex).__name__)
        print(ex)
        
myfunc('example')

----------------------------------------------------------------
#Exception Handling With TRY , EXCEPT , ELSE and FINALLY

def myfunc(x):
    try:
        x=x+5
    except TypeError:
        print('cant add number to string')
    except Exception as ex:
        print('There might be some other error')
        print(type(ex).__name__)
        print(ex)
    else:
        print(x)
    finally:
        print('mandotory excecution')
    
myfunc(1)
myfunc('example')

