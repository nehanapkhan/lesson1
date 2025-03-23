import random
import time

def getRandomDate(startDate,endDate):
    print("printing random date between",startDate,"and",endDate)
    randomgenerator = random.random()
    dateformat = "%m/%d/%Y"

    startTime = time.mktime(time.strptime(startDate,dateformat))
    endTime = time.mktime(time.strptime(endDate,dateformat)) 

    RandomTime = startTime + randomgenerator * (endTime -startTime)
    RandomDate = time.strftime(dateformat,time.localtime(RandomTime))

    return RandomDate
print("randomdate =", getRandomDate("1/1/2016","12/12/2018"))

