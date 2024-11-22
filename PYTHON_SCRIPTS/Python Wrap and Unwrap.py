#PYTHON WRAP AND UNWRAP IN DECORATORS
#decorator Function
def datatype_fnc(fnc_as_param):
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x
    return wrapper

#Function which needs decoration  
@datatype_fnc
def number_fnc(num):
    '''This refers number_fnc'''
    print("This is a Number Function with value: "+ str(num))
    return num

number_fnc(2)

#PYTHON DUNDER ATTRIBUTES WHICH SAVES METADATA

number_fnc.__name__
number_fnc.__doc__
number_fnc.__qualname__
number_fnc
number_fnc.__wrapped__

-----------------------------------------------------------------
#USING @WRAPS IMPORTED FROM FUNCTOOLS IN DECORATORS

from functools import wraps
def datatype_fnc(fnc_as_param):
    @wraps(fnc_as_param)
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x
    return wrapper
    
@datatype_fnc
def number_fnc(num):
    '''This refers number_fnc'''
    print("This is a Number Function with value: "+ str(num))
    return num

#PYTHON DUNDER ATTRIBUTES WHICH SAVES METADATA

number_fnc.__name__
number_fnc.__doc__
number_fnc.__qualname__
number_fnc(2)              #decorated function gets called
number_fnc.__wrapped__
number_fnc.__wrapped__(2)  #undecorated/original function gets called
---------------------------------------------------------------

#DECORATOR NESTING EXAMPLE1
#decorator Function

from functools import wraps
def doubler_fnc(fnc_as_param):
    @wraps(fnc_as_param)
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x*2
    return wrapper

#Function which needs decoration

@doubler_fnc
@doubler_fnc
def number_fnc(num):
    '''This refers number_fnc'''
    print("This is a Number Function with value: "+ str(num))
    return num
    
number_fnc(2)

------------------------------------------------------------------
#DECORATOR NESTING EXAMPLE2
#decorator Function

from functools import wraps
def doubler_fnc(fnc_as_param):
    @wraps(fnc_as_param)
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x*2
    return wrapper

#Function which needs decoration 
   
def tripler_fnc(fnc_as_param):
    @wraps(fnc_as_param)
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x*3
    return wrapper
    
@tripler_fnc
@doubler_fnc
def number_fnc(num):
    '''This refers number_fnc'''
    print("This is a Number Function with value: "+ str(num))
    return num