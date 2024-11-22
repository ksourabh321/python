#PYTHON METHOD OVERRIDING / VARIABLE OVERRIDING
#parent Class
class Student:
    # class variable
    dress_code = 'formal'
    
    # initializer method having object variables
    def __init__(self, stream, timing):
        self.stream = stream           #stream can be science,commerce,arts
        self.timing = timing           #timing can be morning,day,evening
        
    # method to fetch details
    def showStreamDetails(self):
        print("This is "+str(self.stream)+" stream having shift timing as " +str(self.timing))
        # you can also use as below, but you can return only one value as func in method. 
        # return self.stream 
        # return self.timing
    
    # method to modify timing details   
    def changeStreamTiming(self,timing):
        self.timing=timing
        
    # method to modify stream details   
    def changeStream(self,stream):
        self.stream=stream
--------------------------------------------------------------------------------
#child class        
class Scistud(Student):
    # class variable
    dress_code = 'white_formal'
    
    # initializer method having object variables
    def __init__(self, stream, timing,noofsub):
        self.stream = stream           #stream can be science,commerce,arts
        self.timing = timing           #timing can be morning,day,evening
        self.noofsub= noofsub          #total no of subject studied
        
    # method to fetch details
    def showStreamDetails(self):
        print("This is "+str(self.stream)+" stream having shift timing as " +str(self.timing)+" no of subjects: "+str(self.noofsub))
        
    # method to modify timing details   
    def changeStreamTiming(self,timing):
        self.timing=timing   
        print("This is from child class Scistud:new stream timing is :"+str(self.timing))
        
        # method to modify subject details   
    def changeStreamNoofsub(self,noofsub):
        self.noofsub=noofsub
        
---------------------------------------------------------------------------------      
scistud_obj=Scistud('science','morning',5)
scistud_obj.showStreamDetails()
scistud_obj.changeStreamTiming('day')
scistud_obj.changeStream('commerce')
scistud_obj.showStreamDetails()
scistud_obj.changeStreamNoofsub(7)
scistud_obj.showStreamDetails()

scistud_obj.dress_code