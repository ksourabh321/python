#Python for loop with integers

for i in range (1,11,2):
    print(i)


#Python for loop with strings

var='alphabet'
for i in var:
    print(i)
    
#Python for loop with Lists

var = ['abhishek','sam','sandy',5,10,5]
for i in var:
    print(i)
    
#Python for loop with tuple
var = ('abhishek','sam','sandy',5,10,5)
for i in var:
    print(i)
    
#Python for loop with Lists with index

var = ['abhishek','sam','sandy',5,10,5]
for i,j in enumerate(var):
    print(i,j)
    
#Python for loop with tuple with index

var = ('abhishek','sam','sandy',5,10,5)
for i,j in enumerate(var):
    print(i,j)
    
#Python for loop with Dictionary key value    
var = {'name': 'abhishek' , 'age': 30 , 'sal': 50000}
for i in var:
    print(i,var[i])
    
    
-------------------------------------------------------
# CONTINUE , BREAK , PASS
-------------------------------------------------------

#continue
for i in range (1,11,1):
    if i<5:
        continue
    print(i)
    
#break
for i in range (1,11,1):
    if i>5:
        break
    print(i)

#pass
for i in range (1,11,1):
    if i<5:
        pass
    print(i)
        