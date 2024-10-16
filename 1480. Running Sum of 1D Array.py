def runningSum(array):
    arraylength = len(array)
    for i in range(1,arraylength):
        array[i] = array[i] + array[i-1]
    return array

testarray = [1,1,1,1,1]
result = runningSum(testarray)
print(result)