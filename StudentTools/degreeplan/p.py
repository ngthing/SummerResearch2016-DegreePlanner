#MODIFY THE TEMPLATE TO: Gets two numbers from the user, and 
#returns the second value subtracted from the first. 

import subprocess 

def template(n1,n2): 
    number1 = n1 #this gets the first number from the user and stores it in a memory location called number1 
    number2 = n2 #this gets the second number from the user and stores it in a memory location called number2 

    sum = number1 + number2 #this adds together all numbers and stores the result in a memory location called sum 
     
    return sum #this returns the sum of the numbers to the user 
     
     
#END OF YOUR CODE 

test1 = template(2,3) 
test2 = template(3,2) 

if (test1 == -1): 
    print "2 minus 3 is -1, you got it RIGHT!" 
else: 
    print "2 minus 3 is -1, you got: " + str(test1) 
     
if (test2 == 1): 
    print "3 minus 2 is 1, you got it RIGHT!" 
else: 
    print "3 minus 2 is 1, you got: " + str(test2)     
     
if (test1 == -1 and test2 == 1): 
    print "Your code is CORRECT!" 
    result = subprocess.check_output("curl -k    https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=guest-chapter0_1-COMPLETED", shell=True)     
else: 
    print "Please check your code, at least one test case did not pass." 
    result = subprocess.check_output("curl -k    https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=guest-chapter0_1-PROGRESS", shell=True) 
