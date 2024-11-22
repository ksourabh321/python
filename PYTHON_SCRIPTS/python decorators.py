#DECORATION FUNCTION
def datatype_fnc(fnc_as_param):
    def wrapper():
        print("Inside wrapper function")
        fnc_as_param()
    return wrapper

------------------------------------------
#Function Which Needs Decoration
def number_fnc():
    print("This is a Number Function")

number_fnc = datatype_fnc(number_fnc)

number_fnc()

-------------------------------------------
#Function Which Needs Decoration
def string_fnc():
    print("This is a String Function")
    
string_fnc = datatype_fnc(string_fnc)

string_fnc()

-------------------------------------------
@datatype_fnc
def number_fnc():
    print("This is a Number Function")

#number_fnc = datatype_fnc(number_fnc)

number_fnc()

--------------------------------------------
@datatype_fnc
def string_fnc():
    print("This is a String Function")
    
#string_fnc = datatype_fnc(string_fnc)

string_fnc()

-------------------------------------------

def datatype_fnc(fnc_as_param):
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        fnc_as_param(*args, **kwargs)
    return wrapper
    
@datatype_fnc
def number_fnc(num):
    print("This is a Number Function with value: "+ str(num))

#number_fnc = datatype_fnc(number_fnc)

number_fnc(5)

-------------------------------------------------------------

def datatype_fnc(fnc_as_param):
    def wrapper(*args, **kwargs):
        print("Inside wrapper function")
        x=fnc_as_param(*args, **kwargs)
        return x
    return wrapper
    
@datatype_fnc
def number_fnc(num):
    print("This is a Number Function with value: "+ str(num))
    return num

#number_fnc = datatype_fnc(number_fnc)

number_fnc(5)

-------------------------------------------------------------
