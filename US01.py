import datetime

def get_date(IndList):
    list = []
    Today = str(datetime.datetime.today())
    for date in (IndList):
        if date[3][:9] == "BIRT Date":
            Date = str(datetime.datetime.strptime(date[3][10:], '%Y-%m-%d').date())
            list.append(Date)
        else:
            print "N/A"
    
    for count,i in enumerate(list):
        if list[count] > Today:
            continue
        else:
            count = count + 1
    print "US01"
    if count == 12:
        print "All dates are correct"
    else:
        print count , "Error"