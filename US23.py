import datetime 

def uniqueIndividuals(IndList):
    uniquePerson = dict()
    flag = False
    for date in (IndList):
        if date[1][:4] == "NAME":
            name = date[1][5:]
        date1 = date[3][10:].strip()
        birt_date = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
        if name in uniquePerson and birt_date in uniquePerson.values():
            print " Repeated Name " + name + " and Birthdate "  + str(birt_date)
            flag = True
        else:
            uniquePerson[name] = birt_date
    if flag == False:
        print "All name + birthdate pairs are unique"