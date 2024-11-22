#PYTHON SUPER CLASS
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
    
--------------------------------------------------------------------------------
#child class        
class Scistud(Student):
    # class variable
    dress_code = 'white_formal'
    
    # initializer method having object variables
    def __init__(self, stream, timing,noofsub):
        super().__init__(stream,timing)
        #self.stream = stream           #stream can be science,commerce,arts
        #self.timing = timing           #timing can be morning,day,evening
        self.noofsub= noofsub           #total no of subject studied
        
    # method to fetch details
    def showStreamDetails(self):
        super().showStreamDetails()
        print("This is "+str(self.stream)+" stream having shift timing as " +str(self.timing)+" no of subjects: "+str(self.noofsub))
        
        
---------------------------------------------------------------------------------      
scistud_obj=Scistud('science','morning',5)
scistud_obj.showStreamDetails()
---------------------------------------------------------------------------------