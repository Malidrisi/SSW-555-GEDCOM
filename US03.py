import datetime 

def birthBeforeDeath(IndList,wr):
    flag = False
    wr.write("\n\nUS01 - Date before current date\n")
    for date in (IndList):
        if date[4][10:] == "Alive":
            pass
        else:
            if date[1][:4] == "NAME":
                name = date[1][5:]
                #print name
            date1 = date[3][10:].strip()
            birt_date = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
            date2 = date[4][10:].strip()
            deat_date = datetime.datetime.strptime(date2,'%Y-%m-%d').date()
            if birt_date > deat_date:
                output = "Birth " + str(birt_date) +" should occur before death" + str(deat_date)
                wr.write(output)
                flag = True
    if flag == False:
        wr.write("All births occur before deaths!")