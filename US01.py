import datetime

def get_date(IndList,wr):
    list = []
    Today = str(datetime.datetime.today())
    wr.write("\n\nUS01 - Date before current date")
    for date in (IndList):
        if date[3][:9] == "BIRT Date":
            Date = str(datetime.datetime.strptime(date[3][10:], '%Y-%m-%d').date())
            list.append(Date)
        else:
            wr.write("/nN/A")
    
    for count,i in enumerate(list):
        if list[count] > Today:
            continue
        else:
            count = count + 1
    if count == 12:
        wr.write("\nAll dates are correct")
    else:
        wr.write("\nError")

