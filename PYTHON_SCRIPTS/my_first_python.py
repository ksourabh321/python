def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
        print ("new sal of emp_id : " + str(emp_id) + " is " + str(sal))
    elif years > 3 :
        sal = sal + 100000
        print ("new sal of emp_id : " + str(emp_id) + " is " + str(sal))
    else :
        sal = sal + 50000
        print ("new sal of emp_id : " + str(emp_id) + " is " + str(sal))

incrementempsal(10,50000,10)
