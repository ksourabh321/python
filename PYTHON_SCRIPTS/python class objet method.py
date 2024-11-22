# Normal function def and execution
def doubler(n):
    return n*2

doubler(10)
  
x=doubler(10)
print(x)

----------------------------------------
# CLASS , OBJECT AND METHOD
----------------------------------------

class Student:
    # class variable
    dress_code = 'formal'
    
    # initializer method having object variables
    def __init__(self, stream, timing):
        self.stream = stream           #stream can be science,commerce,arts
        self.timing = timing           #timing can be morning,day,evening
        
    # method to fetch details
    def showStreamTiming(self):
        print("This is "+str(self.stream)+" stream having shift timing as " +str(self.timing))
        # you can also use as below, but you can return only one value as func in method. 
        # return self.stream 
        # return self.timing
    
    # method to modify details   
    def changeStreamTiming(self,timing):
        self.timing=timing

#create object sci_stud        
sci_stud=Student('science','morning')

#call method to fetch details
sci_stud.showStreamTiming()

# call method to modify details
sci_stud.changeStreamTiming('day')

#call method to fetch details
sci_stud.showStreamTiming()

#call class variable
print(sci_stud.dress_code)
print(Student.dress_code)

#delete object variables / objects itself
del sci_stud.dress_code
del sci_stud.stream
del sci_stud