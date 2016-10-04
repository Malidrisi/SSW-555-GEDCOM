import datetime 

def birthBeforeDeath(IndList):
    for date in (IndList):
        if date[4][10:] == "Alive":
            pass
        else:
            if date[1][:4] == "NAME":
                name = date[1][5:]
                print name
            date1 = date[3][10:].strip()
            birt_date = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
            date2 = date[4][10:].strip()
            deat_date = datetime.datetime.strptime(date2,'%Y-%m-%d').date()
            if birt_date > deat_date:
                print "Birth " + str(birt_date) +" should occur before death" + str(deat_date)


        




