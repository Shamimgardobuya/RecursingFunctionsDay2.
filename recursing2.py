  #1. Write a Python program to calculate the sum of a list of numbers. using recursion Go to the editor
#create a list of numers
#one can use inbuilt function 
#loopthrough the list 
#create a variable that will hold the sum of the values 
#using recursion 
   #do we need an if stmt when recursing
   #do we use recursing for looping
def summing(number):
    added=0
    if (number==0):
        return 0
    else:
        for i in range(number+1):     #finding each number in list 
            summing(number-i)   #to go to number before
            added+=number
            print(added)
summing([4,6,8])
        


    
