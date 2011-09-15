import itertools, datetime

def isLeapYear(year):
    retVal = year%4 == 0
    if (year%4==0 and year%100==0 and not year%400==0):
        retVal = False
    return retVal

def convertToNumbers(datestring):
    a,b,c= datestring.split('/')
    return [int(a), int(b), int(c)]

def isDate(year,month,day):
    retVal = False
    try:
        datetime.date(year,month,day)
        retVal = True
    except ValueError:
        pass
    return retVal

def lowestDate(indata):
    
    tempDates = itertools.permutations(convertToNumbers(indata))
    validDates = []

    for testDate in tempDates:
        if isDate(testDate[0],testDate[1],testDate[2]):
            year = testDate[0] if testDate[0] > 1000 else testDate[0] + 2000
            validDates.append(datetime.date(year, testDate[1], testDate[2]))

    retVal = [0,0,0]

    if len(validDates) > 0:
        lowest = sorted(validDates)[0]
        retVal = [lowest.year, lowest.month, lowest.day]
    return retVal
