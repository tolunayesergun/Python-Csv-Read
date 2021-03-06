from Modules import functionsModule as fm
import csv

table = csv.DictReader(open('data/owid-covid-data.csv'))
locationList = []
caseList = []

for row in table:
    if fm.ElementIsNotExist(row["location"],locationList):fm.AddToLists(row["location"],locationList,caseList)
    else: fm.FindBiggerValue(row["total_cases"],caseList)

fm.PrintResults(20,locationList,caseList)