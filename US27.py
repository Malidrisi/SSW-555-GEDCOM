import datetime

def individual_ages(IndList):
    for date in (IndList):
        if date[1][:4] == "NAME":
            name = date[1][5:]
            print "Name: ", name
        else:
            "N/A"
        if date[3][:9] == "BIRT Date":
            my_date = date[3][10:].strip()
            Date = datetime.datetime.strptime(my_date,'%Y-%m-%d')
            Today = datetime.datetime.today()
            age = (Today - Date).days/365
            if age < 0:
                print "ERROR : Birthdate for " + name +" cannot be after " + str(Today)
            else:
                print "Age : %d" % (age)


