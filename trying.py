# binding.rvFibo.layoutManager=LinearLayoutManager(this)
#         binding.rvFibo.adapter=fibonacciAdapterView(numbList)


def removing(number):
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
        removing(number+z)
        # summing(number-1)
        # number+=1
            


        # added+=z


            # summing(number[i]-1)
        # print(''.join(number))
        print(number)

removing(3)
