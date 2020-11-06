#from GoogleNews import GoogleNews
from pandas import DataFrame
from datetime import timedelta  
from dateutil.relativedelta import *
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import datetime

## set up day variables 

xday = 1
xmonth = 1
xyear = 2010
x2day = xday
x2month = xmonth + 1
x2year = xyear

## set up date strings

xdate = str(xday) + "/" + str(xmonth) + "/" + str(xyear)
x2date = str(xday) + "/" + str(x2month) + "/" + str(x2year)


## set up while loop varibales 
loopcount = 1
totalloopcount = 1
newscount = 0
totalnewscount = 0


## main loop, each loopcount, one year

while loopcount <= 1 :


## sub-loop, each month

    while totalloopcount <= 12:

## google news configure search
      
        googlenews = GoogleNews()
        googlenews.setlang('en')
        googlenews.setperiod('d')
        googlenews.setTimeRange(xdate,x2date)
        googlenews.setencode('utf-8')
        googlenews.search('Apple stock')
       
## print out each month number of news articles

        print ("xdate:" + xdate)
        print ("x2date:" + x2date)
        for i in range(1,20):
            googlenews.getpage(i)
            result=googlenews.result()
            df=pd.DataFrame(result)
        print ("count:")
        print (df['title'].count() )
        newscount += df['title'].count() 
        loopcount += 1
        xmonth += 1
        x2month += 1
        xdate = str(xday) + "/" + str(xmonth) + "/" + str(xyear)
        x2date = str(xday) + "/" + str(x2month) + "/" + str(x2year)
        totalloopcount += 1

## each year will display total count of news articles     

    print ("-----")
    print ("newscount:")
    print ( newscount )
    loopcount += 1
    totalnewscount += newscount
    print ("totalnewscount:")
    print (totalnewscount)
    print ("yearstart:")
    print ( xyear )
    print ("-----")

## set current newscount to 0 to reset for each year

    newscount = 0

 
googlenews.clear()
