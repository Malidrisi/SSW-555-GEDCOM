import datetime

def get_age(IndList):
    print "US27"
    for date in (IndList):
        if date[1][:4] == "NAME":
            print "Name: ",date[1][5:]
        else:
            "N/A"
        if date[3][:9] == "BIRT Date":
            my_date = date[3][10:].strip()
            Date = datetime.datetime.strptime(my_date,'%Y-%m-%d')
            print "Birthdate: " , Date
            print "Age : %d" % ((datetime.datetime.today() - Date).days/365)
        else:
            "N/A"

