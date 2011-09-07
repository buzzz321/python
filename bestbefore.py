# -*- coding: utf-8 -*-
'''
Created on 5 sep 2011

@author: anders
'''
import datetime, sys

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
  data=sorted(indata)

  if data[2] > 31:
    data.insert(0,data.pop(2))

  if data[0] < 2000:
    data[0] = 2000 + data[0]

  if isDate(data[0], data[1], data[2]):
    retVal = data
  else:
    retVal = [0,0,0]

  return retVal

if __name__ == '__main__':
  if len(sys.argv) == 2:
    infile = open(sys.argv[1],'r')
    datestring = infile.readline()

    datearray = convertToNumbers(datestring.strip())
    datearray=lowestDate(datearray)
    
    if datearray !=[0,0,0]:
      print "{0}-{1:02d}-{2:02d}".format(datearray[0], datearray[1], datearray[2])
    else:
      print datestring.strip() + " is illegal" 

  else:
    print "Please run with an input file"
  pass
