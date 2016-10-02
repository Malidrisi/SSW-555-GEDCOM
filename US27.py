from datetime import datetime

with open('/Users/rafifarab/Desktop/GEDCOM/data.ged', 'r') as f:
    for i in (f):
        words = i.split()

        if words[0] == '1' and words[1] == 'NAME':
            List = i[7:].strip().replace('/','')
            print "Name:" + " " + List
        
        if words[1] == 'BIRT' and words[1] != 'DEAT':
            Date = next(f)
            my_date = Date[6:].strip()
            NewDate = datetime.strptime(my_date, '%d %b %Y')
            print "Birthdate: " , NewDate
            print "Age : %d" % ((datetime.today() - NewDate).days/365) 