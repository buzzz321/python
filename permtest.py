import alternate, bestbefore, itertools, random


for i in range(100000):
    year = random.randrange(0, 2999)
    n1 = random.randrange(1, 99)
    n2 = random.randrange(1, 99)

    temp = [year, n1, n2]
    temp = itertools.permutations(temp)
    
    for date in temp:
        testString="{0}/{1}/{2}".format(date[0], date[1], date[2])

        altDate = alternate.lowestDate(testString)
        bestDate = bestbefore.lowestDate(bestbefore.convertToNumbers(testString))

        if altDate != bestDate :
            print "teststring=",testString, " ", altDate , " != " , bestDate

