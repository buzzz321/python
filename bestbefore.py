'''
Created on 5 sep 2011

@author: anders
'''
import datetime

def isLeapYear(year):
    retVal = year%4 == 0
    if (year%4==0 and year%100==0 and not year%400==0):
        retVal = False
    return retVal

def convertToNumbers(datestring):
    a,b,c= datestring.split('/')
    return (int(a), int(b), int(c))

def isDate(year,month,day):
    retVal = False
    try:
        datetime.date(year,month,day)
        retVal = True
    except ValueError:
        pass
    return retVal

def isYear(number):
    retVal = False
    
    if number == 0 or number > 31:
        retVal = True
    
    return retVal

if __name__ == '__main__':
    pass