-------------------------------------------------------------------------
def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
    elif years > 3 :
        sal = sal + 100000
    else:
        sal = sal + 50000
    print ("new sal of emp_id : " + str(emp_id) + " is " + str(sal))
	return sal

incrementempsal(10,50000,5)
--------------------------------------------------------------------------    
def incrementempsal(emp_id: int,sal: int,years: int) -> int:
    if years > 5 :
        sal = sal + 200000
    elif years > 3 :
        sal = sal + 100000
    else :
        sal = sal + 50000
    print ("new sal of emp_id : " + str(emp_id) + " is " + str(sal))
    return sal

incrementempsal(10,50000,5)        
-------------------------------------------------------------------------
