import datetime
def get_date(IndList):
    
    List = []

<<<<<<< Updated upstream
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
    if count == 12:
        print "All dates are correct"
    else:
        print count , "Error"
=======
    my_file = open('/Users/rafifarab/Desktop/GEDCOM/data.ged', 'r')
    for lines in my_file:
        words = lines.split()
        if words[1] in ['BIRT','DEAT','DIV', 'MARR']:
            DateType = words[1]
        
        elif words[0] == "2" and words[1] == "DATE":
            List = [DateType + ' DATE ' + str(datetime.datetime.strptime(lines[7:].strip(), '%d %b %Y').date())] 
        
            Date = List[0][10:]
            today = str(datetime.datetime.now())
        
    if today > Date:
            print "All Date are correct"
    else:
            print "Error: Date is not correct"
>>>>>>> Stashed changes
