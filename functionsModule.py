def ElementIsNotExist(_element,array):
    for element in array:
        if _element == element:
            return False
    return True

def AddToLists(_value,firstArray,secondArray):
    firstArray.append(_value)
    secondArray.append("0")


def FindBiggerValue(_value,array):
    try:
        if float(_value) > float(array[len(array)-1]):
            array[len(array)-1] = _value
    except ValueError:
        pass


def SortArrays(firstArray,secondArray):
    n = len(secondArray)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(secondArray[j]) < float(secondArray[j+1]):
                firstArray[j], firstArray[j+1] = firstArray[j+1], firstArray[j]
                secondArray[j], secondArray[j+1] = secondArray[j+1], secondArray[j]
                

def PrintResults(_length,firstArray,secondArray):
    SortArrays(firstArray,secondArray)
    for i in range(_length):
        print(firstArray[i]+" "+secondArray[i])