import datetime

TempRec = []

my_file = open('/Users/rafifarab/Desktop/GEDCOM/data.ged', 'r')
for lines in my_file:
    words = lines.split()
    if words[1] in ['BIRT','DEAT','DIV', 'MARR']:
        DateType = words[1]
        
    elif words[0] == "2" and words[1] == "DATE":
        TempRec = [DateType + ' DATE ' + str(datetime.datetime.strptime(lines[7:].strip(), '%d %b %Y').date())] 
        print TempRec
        Date = TempRec[0][10:]
        today = str(datetime.datetime.now())
        
        if today > Date:
            print "Date is correct"
        else:
            print "Error: Date is not correct"
