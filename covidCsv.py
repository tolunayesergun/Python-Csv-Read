locationList = []
caseList = []

def LocationIsExist(_location):
    for location in locationList:
        if _location == location:
            return False
    return True


def AddToLists(_firstValue):
    locationList.append(_firstValue)
    caseList.append("0")


def FindBiggerCase(_currentCase):
    try:
        if float(_currentCase) > float(caseList[len(caseList)-1]):
            caseList[len(caseList)-1] = _currentCase
    except ValueError:
        pass


def SortArrays():
    n = len(caseList)
    for i in range(n):
        for j in range(0, n-i-1):
            if float(caseList[j]) < float(caseList[j+1]):
                caseList[j], caseList[j+1] = caseList[j+1], caseList[j]
                locationList[j], locationList[j+1] = locationList[j+1], locationList[j]


def PrintResults(_length):
    SortArrays()
    for i in range(_length):
        print(locationList[i]+" "+caseList[i])
        if i == 20: break
