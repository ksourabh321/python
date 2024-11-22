#Python for loop with integers
for i in range (1,11,1):
    print(i)
	
#Python while loop with integers
i=1
while(i<11):
	print(i)
	i= i+1
    
-----------------------------------------
#Python for loop with strings

var='alphabet'
for i in var:
    print(i)
 
#Python while loop with strings 
var='alphabet'
i=0
while(i<len(var)):
	print(var[i])
	i= i+1

-------------------------------------
#Python for loop with Lists

var = ['abhishek','sam','sandy',5,10,5]
for i in var:
    print(i)

#Python while loop with Lists    
var=['abhishek','sam','sandy',5,10,5]
i=0
while(i<len(var)):
	print(var[i])
	i= i+1
---------------------------------------
#Python for loop with tuple

var = ('abhishek','sam','sandy',5,10,5)
for i in var:
    print(i)

#Python while loop with Lists    
var=('abhishek','sam','sandy',5,10,5)
i=0
while(i<len(var)):
	print(var[i])
	i= i+1   
---------------------------------------
#Python do while loop with Lists 
var=['abhishek','sam','sandy',5,10,5]
i=0
while True:
    print(var[i])
    i= i+1
    if i>=len(var):
        break
        
---------------------------------------
#python control statement in do while loop
var=['abhishek','sam','sandy',5,10,5]
i=0
while True:
    print(var[i])
    i= i+1
    if i<len(var):
        continue
    else:
        break