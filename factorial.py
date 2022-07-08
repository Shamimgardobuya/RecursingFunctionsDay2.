# def summing(number):
#     z=number-2
#     print(number)
#     # added=0
#     # added+=number
#     # z=added+number
#     # print(z)
#     # print(added)
#     # print(number)
#     # number=[4,6,8]
#     if number==0:
#         return 0
#     else:
#         i=0
#         # p=len(number)
#         # while i<p:
#         # added+=number
#         summing(number+z)
#         # summing(number-1)
#         # number+=1
            


#         # added+=z


#             # summing(number[i]-1)
#         # print(''.join(number))
#         print(number)

# summing(3)
  #create function and pass in a number
  #using recursion
#finding factorial of a number using recursion
 #create a function and pass in a parameter
 #loop througheach of the number
 #create a default varible and assign it the multiplied variable to our new variable
 #print the new variable
 #call function


def factorial(x):
  fact=1
  for i in range(1,x+1,1):
    fact*=i
  print(fact)
factorial(7)
 
def facto(y):
  # factorial=1
  # print(x)
  if y==1:    #made,starting point to be one 
    return 1
  else:
    return (y * facto(y-1))
    
ans=facto(5)
print(ans)


