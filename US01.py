from datetime import date
import datetime

def date_before_current_date(IndList,wr):
    l = []
    error_date = []
    Today = date.today() 
    wr.write("\n\nUS01 - Date before current date")
    for d in (IndList):
        bDate = d[3][10:]
        l.append(bDate)
        if d[4][10:] == "Alive":
            continue
        else:
            dDate = d[4][10:]
            l.append(dDate)
    count = 0
    
    for index,i in enumerate(l):
        if Today > datetime.datetime.strptime(l[index], '%Y-%m-%d').date():
            continue
        else:
            error_date = error_date + [l[index]]
            count = count+1
    if count == 0:
        wr.write ("\nAll dates are correct")
    else:
        numb_of_ind = str(count)
        output = "\n" + numb_of_ind + " date are after " + str(Today)  + str(error_date)
        wr.write(output)