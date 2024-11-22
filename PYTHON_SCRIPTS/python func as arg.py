# PYTHON FUNCTION AS AN ARGUMNENT
def number_fnc():
    print("This is a Number Function")

def string_fnc():
    print("This is a String Function")

def datatype_fnc(fnc_as_param):
    fnc_as_param()
    
datatype_fnc(number_fnc)
datatype_fnc(string_fnc)
--------------------------------------------------------
# PYTHON FUNCTION DEFINED AND CALLED IN ANOTHER FUNCTION

def number_fnc():
    print("This is a Number Function")
    def int_fnc():
        print("This is an Integer Function")
    int_fnc()

number_fnc()

--------------------------------------------------------
# PYTHON FUNCTION AS RETURN TYPE

def number_fnc():
    print("This is a Number Function")
    def int_fnc():
        print("This is an Integer Function")
    return int_fnc

x=number_fnc()
print(x())

   