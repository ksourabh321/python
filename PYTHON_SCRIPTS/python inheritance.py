#INHERITANCE PROPERTIES
#parent Class
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
--------------------------------------------------------------------------------
#child class        
class Scistud(Student):
    
    # initializer method having object variables
    def __init__(self, stream, timing,noofsub):
        self.stream = stream           #stream can be science,commerce,arts
        self.timing = timing           #timing can be morning,day,evening
        self.noofsub= noofsub          #total no of subject studied
        
    # method to fetch details
    def showStreamdetails(self):
        print("This is "+str(self.stream)+" stream having shift timing as " +str(self.timing)+" no of subjects: "+str(self.noofsub))
        
    # method to modify subject details   
    def changeStreamNoofsub(self,noofsub):
        self.noofsub=noofsub
    
    # method to modify timing details   
    def changeStreamTimingChild(self,timing):
        self.timing=timing     
        
-----------------------------------------------------------------------------------
scistud_obj=Scistud('science','morning',5)
scistud_obj.showStreamTiming()
scistud_obj.showStreamdetails()
scistud_obj.dress_code
scistud_obj.changeStreamTiming('day')
scistud_obj.showStreamTiming()
scistud_obj.showStreamdetails()
scistud_obj.changeStreamNoofsub(7)
scistud_obj.showStreamdetails()
scistud_obj.changeStreamTimingChild('evening')
scistud_obj.showStreamTiming()
------------------------------------------------------------------------------------

