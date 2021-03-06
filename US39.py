from datetime import date, timedelta
import datetime
def IsAlive(ID,IndList):
    for ind in IndList:
        if ind[0] == ID:
            if ind[4][10:] == "Alive":
                return True
            else:
                return False
def ListUpcomingAnn(FamList,IndList,wr):
    count= 0
    wr.write("\n\nUS39 - List Upcoming Anniversaries")
    result =[]
    for daterange in range(30):
        result = result + [(datetime.datetime.now().date() + timedelta(daterange))]
    for Fam in FamList:        
        if Fam[-1][:3] == "DIV":
            pass
        else: 
            if IsAlive(Fam[1][5:],IndList) and IsAlive(Fam[2][5:],IndList):
                MarDate= datetime.datetime.strptime(Fam[-1][10:], '%Y-%m-%d').date()
                today= date.today() 
                AnnDate= datetime.date(today.year, MarDate.month, MarDate.day)
                if 0 <= (AnnDate - today).days <= 30:
                    count= count+1
                    output= "\nThe Anniversary for family " + Fam[0] + " is in " + str(AnnDate)
                    wr.write(str(output))
    if count == 0:
        wr.write("\nNo Upcoming Anniversary")