#PYTHON USER DEFINED/CUSTOM EXCEPTION
-----------------------------------------------------
# Create and raise Custom exception 'myexception'
class MyException(Exception):
    pass

raise MyException('My Custom Exception')

------------------------------------------------------

class MyException(Exception):

    def __init__(self, message, exc_err_cd):
        super().__init__(message)
        self.message=message
        self.exc_err_cd = exc_err_cd

    def __str__(self):
        return "This is custom exception "+str(self.exc_err_cd)+" with msg as " +str(self.message)
    
    def myerrormethod(self):
        return "This is my error method"
    
--------------------------------------------------------------------
def myfunc(x):
    try:
        if x==0:
            raise MyException("Division by zero is not allowed",200)
        else:
            return 100/x
    except MyException as ex:
        print(type(ex).__name__)
        print(ex)
        print(ex.myerrormethod())
---------------------------------------------------------------------        