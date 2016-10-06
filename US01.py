import datetime
def date_before_current_date(IndList,wr):
    list = []
    Today = str(datetime.datetime.today())
    wr.write("\n\nUS01 - Date before current date")
    for date in (IndList):
        if date[3][:9] == "BIRT Date" and date[4][10:] == "Alive":
            my_date = date[3][10:]
            BirthDate = "Birthdate " + str(datetime.datetime.strptime(my_date,'%Y-%m-%d'))
            list.append(BirthDate)
        else:
            my_date = date[4][10:]
            DeathDate = "Deathdate " + str(datetime.datetime.strptime(my_date,'%Y-%m-%d'))
            list.append(DeathDate)
    count = 0
    for index,i in enumerate(list):
        if Today > list[index][10:]:
            continue
        else:
            error_date = list[index][10:]
            count = count+1
    if count == 0:
        wr.write ("\nAll dates are correct")
    else:
        wr.write("\nError: date ",error_date + " " + "cannot be after " + Today)
