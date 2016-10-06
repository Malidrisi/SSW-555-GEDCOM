import datetime 

def uniqueIndividuals(IndList,wr):
    uniquePerson = dict()
    flag = False
    wr.write("\n\nUS23 - Unique names and birthdates")
    for ind in (IndList):
        name = ind[1][5:]
        date1 = ind[3][10:].strip()
        birt_date = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
        if name in uniquePerson and birt_date in uniquePerson.values():
            output= "\nRepeated Name " + name + " and Birthdate "  + str(birt_date)
            wr.write(output)
            flag = True
        else:
            uniquePerson[name] = birt_date
    if flag == False:
        wr.write("\nAll name + birthdate pairs are unique")