from datetime import date
import datetime

def getAge(Ind):
    if Ind[4][10:] == "Alive":
        return ((date.today() - datetime.datetime.strptime(Ind[3][10:], '%Y-%m-%d').date()).days/365)
    else:
        return ((datetime.datetime.strptime(Ind[4][10:], '%Y-%m-%d').date() - datetime.datetime.strptime(Ind[3][10:], '%Y-%m-%d').date()).days/365)
         
def age_less_than_150(IndList):
    n=0
    for ind in IndList:
        if getAge(ind) < 150:
            pass
        else:
            n=n+1
    print "US07"
    if n == 0:
        print "All individuals are less than 50 years old"    
    else:
        print n, "Individuals are more than 50 years old" 
        