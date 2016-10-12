from datetime import datetime, timedelta
import datetime

result =[]
now = datetime.datetime.now().date()
for daterange in range(30):
    result = result + [(now + timedelta(daterange))]
   
def GetDate(birthday):
    if birthday[4][10:] == "Alive":
        return (datetime.datetime.strptime(birthday[3][10:].strip(), '%Y-%m-%d').date())
    else:
        pass
        
def UpcomingBirthday(IndList,wr):
    flag = False
    wr.write("\n\nUS38  - Upcoming Birthdays")
    DOB = []
    for ind in IndList:
        if GetDate(ind) in result:
            DOB = DOB + [str(GetDate(ind))]
            flag = True
        else:
            continue
                   
    if flag == False:
        wr.write ("\nNo upcoming birthdays")
    else:
        output = "\nUpcoming birthdays" + str(DOB)
        wr.write(output)