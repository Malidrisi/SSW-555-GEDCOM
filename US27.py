import datetime

def individual_ages(IndList,wr):
    wr.write("\n\nUS27 - Include individual ages")
    for date in (IndList):
        if date[1][:4] == "NAME":
            name= "\nName: " + date[1][5:]
            wr.write(name)
        else:
            wr.write("\nN/A")
        if date[3][:9] == "BIRT Date":
            my_date = date[3][10:].strip()
            Date = datetime.datetime.strptime(my_date,'%Y-%m-%d')
            Today = datetime.datetime.today()
            age = (Today - Date).days/365
            if age < 0:
                wr.write(" --ERROR : Age cannot be after today")
            else:
                output = " - Age: %d" % ((datetime.datetime.today() - Date).days/365)
                wr.write(output)
        else:
            wr.write("\nN/A")