import matplotlib.pyplot as plt
import numpy as np


def ElementIsNotExist(_element, array):
    for element in array:
        if _element == element:
            return False
    return True


def AddToLists(_value, firstArray, secondArray):
    firstArray.append(_value)
    secondArray.append("0")


def FindBiggerValue(_value, array):
    try:
        if float(_value) > float(array[len(array)-1]):
            array[len(array)-1] = _value
    except ValueError:
        pass


def SortArrays(firstArray, secondArray):
    n = len(secondArray)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(secondArray[j]) < float(secondArray[j+1]):
                firstArray[j], firstArray[j+1] = firstArray[j+1], firstArray[j]
                secondArray[j], secondArray[j +
                                            1] = secondArray[j+1], secondArray[j]


def Graph(firstArray, secondArray):
    firstArray = np.flip(firstArray[1:20])
    secondArray = np.flip(secondArray[1:20])
    array_float = np.array(secondArray, dtype='float')
    array_int = np.array(array_float, dtype='int')
    plt.figure(figsize=(10, 5))
    plt.title('Total Cases of the 20 Countries')
    plt.xlabel("Countries")
    plt.ylabel("Total Cases")
    plt.bar(firstArray, array_int, color="blue")
    plt.xticks(rotation=90, fontsize=11)
    plt.show()


def PrintResults(_length, firstArray, secondArray):
    SortArrays(firstArray, secondArray)
    for i in range(_length):
        print(firstArray[i]+" "+secondArray[i])
    Graph(firstArray, secondArray)