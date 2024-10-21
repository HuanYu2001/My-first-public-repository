def FizzBuzz(n):
    FBlist = []
    for i in range(1,n+1):
        if(i % 3 ==0 and i % 5 ==0):
            FBlist.append("FizzBuzz")
        elif(i % 3 == 0):
            FBlist.append("Fizz")
        elif(i % 5 == 0):
            FBlist.append("Buzz")
        else:
            FBlist.append(i)
    return FBlist

result = FizzBuzz(20)
print(result)