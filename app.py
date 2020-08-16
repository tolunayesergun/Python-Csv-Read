import csv
import covidCsv as ccs

corona = csv.DictReader(open('owid-covid-data.csv'))

for row in corona:
    if ccs.LocationIsExist(row["location"]):
        ccs.AddToLists(row["location"])
    else:
        ccs.FindBiggerCase(row["total_cases"])


ccs.PrintResults(10)