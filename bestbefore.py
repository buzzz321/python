'''
Created on 5 sep 2011

@author: anders
'''
import datetime, sys, itertools

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
    allDates = itertools.permutations(indata)
    validDates = []

    for testDate in allDates:
        year = testDate[0] if testDate[0] >= 2000 else testDate[0] + 2000
        if isDate(year,testDate[1],testDate[2]):
            validDates.append(datetime.date(year, testDate[1], testDate[2]))

    retVal = [0,0,0]
    
    if len(validDates) > 0:
        lowest = sorted(validDates)[0]
        retVal = [lowest.year, lowest.month, lowest.day]
    return retVal

if __name__ == '__main__':
    datestring = sys.stdin.readline()

    datearray = convertToNumbers(datestring.strip())
    datearray=lowestDate(datearray)

    if datearray !=[0,0,0]:
        print "{0}-{1:02d}-{2:02d}".format(datearray[0], datearray[1], datearray[2])
    else:
        print datestring.strip() + " is illegal" 
