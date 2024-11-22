# IF ELIF ELSE In Function (print syntax one)

def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
        print ('new sal of emp_id : ' + str(emp_id) + ' is ' + str(sal))
    elif years > 3 :
        sal = sal + 100000
        print ('new sal of emp_id : ' + str(emp_id) + ' is ' + str(sal))
    else:
        sal = sal + 50000
        print ('new sal of emp_id : ' + str(emp_id) + ' is ' + str(sal))

incrementempsal(10,20000,6)
-------------------------------------------------------------------------
# IF ELIF ELSE In Function (print syntax two)

def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
        print(f'new sal of emp_id : {emp_id} is {sal}')
    elif years > 3 :
        sal = sal + 100000
        print(f'new sal of emp_id : {emp_id} is {sal}')
    else:
        sal = sal + 50000
        print(f'new sal of emp_id : {emp_id} is {sal}')

incrementempsal(10,20000,6)        
-------------------------------------------------------------------------
# NESTED IF

def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
        if years > 5 :
            print ('new sal of emp_id : ' + str(emp_id) + ' is ' + str(sal))
            
incrementempsal(10,20000,6)
-------------------------------------------------------------------------
# CASE Statement In Function (Syntax one)

def emp_shift(shift):
    match shift:
        case 'morning':
            print '5 AM'
        case 'day':
            print '10 AM'    
        case 'evening':
            print '4 PM'
        case 'night':
            print '10 PM'
        case _:
            print 'It is a not a valid shift'

--------------------------------------------------------------------------  
# CASE Statement In Function (Syntax two)

def emp_shift(shift):
    match shift:
        case shift if shift == 'morning':
            print '5 AM'
        case shift if shift == 'day':
            print '10 AM'    
        case shift if shift == 'evening':
            print '4 PM'
        case shift if shift == 'night':
            print '10 PM'
        case _:
            print 'It is a not a valid shift'

    
--------------------------------------------------------------------------            
# SWITCH CASE Statement In Function (Syntax three)
    
def emp_shift(shift):
    switch={
       'morning': '5 AM',
       'day':     '10 AM',
       'evening': '4 PM',
       'night':   '10 PM'
       }
    print (switch.get(shift,'It is a not a valid shift'))