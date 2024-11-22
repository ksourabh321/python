def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
        if years > 5 :
            print ('new sal of emp_id : ' + str(emp_id) + ' is ' + str(sal))

incrementempsal(10,20000,6)
