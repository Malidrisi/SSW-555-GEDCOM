from datetime import date
import datetime

def getAge(Ind):
    if Ind[4][10:] == "Alive":
        return ((date.today() - datetime.datetime.strptime(Ind[3][10:], '%Y-%m-%d').date()).days/365)
    else:
        return ((datetime.datetime.strptime(Ind[4][10:], '%Y-%m-%d').date() - datetime.datetime.strptime(Ind[3][10:], '%Y-%m-%d').date()).days/365)
         
def age_less_than_150(IndList,flag,wr):
    n=0
    wr.write("\n\nUS07 - Less then 150 years old")
    for ind in IndList:
        if getAge(ind) < 150:
            pass
        else:
            n=n+1
    if flag == 1:
        
        if n == 0:
            wr.write("\nAll individuals are less than 50 years old")
        else:
            output= "\n",n, "Individuals are more than 50 years old"
            wr.write(output)
    else:
        return n
        