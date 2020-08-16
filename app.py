import csv

corona = csv.DictReader(open('owid-covid-data.csv'))
locationList = []
caseList = []
currentLocationIndex = -1


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
        if float(_currentCase) > float(caseList[currentLocationIndex]):
            caseList[currentLocationIndex] = _currentCase
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


for row in corona:
    if LocationIsExist(row["location"]):
        AddToLists(row["location"])
        currentLocationIndex += 1
    else:
        FindBiggerCase(row["total_cases"])


PrintResults(20)