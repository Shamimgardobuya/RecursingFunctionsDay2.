  #1. Write a Python program to calculate the sum of a list of numbers. using recursion Go to the editor
#create a list of numers
#one can use inbuilt function 
#loopthrough the list 
#create a variable that will hold the sum of the values 
#using recursion 
   #do we need an if stmt when recursing
   #do we use recursing for looping
   #he only requirement for a function to be considered recursive is the existence of a code path through which it calls itself, directly or indirectly. All correct recursive functions also have a conditional of some sort, preventing them from "recursing down" forever.


def summing(number):
    z=number-2
    print(number)
    # added=0
    # added+=number
    # z=added+number
    # print(z)
    # print(added)
    # print(number)
    # number=[4,6,8]
    if number==0:
        return 0
    else:
        i=0
        # p=len(number)
        # while i<p:
        # added+=number
        summing(number+z)
        # summing(number-1)
        # number+=1
            


        # added+=z


            # summing(number[i]-1)
        # print(''.join(number))
        print(number)

summing(3)



        # for i in summing(number[]):
        #     added+=i
        # print(added)
        #   i=number[0]
        #  number[i]
            #finding each number in list 
                      #to go to number before
        #finding 


    
