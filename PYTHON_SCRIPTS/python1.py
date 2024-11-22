def incrementempsal(emp_id,sal,years):
    if years > 5 :
        sal = sal + 200000
    elif years > 3 :
        sal = sal + 100000
    else:
        sal = sal + 50000
    return sal
    
def wrapper_func(id,pay,exper):
    res=incrementempsal(id,pay,exper)
    return res
    
    
if __name__=="__main__":
    print(wrapper_func(10,50000,5))
else:
    print("no run for python1")
    
    
