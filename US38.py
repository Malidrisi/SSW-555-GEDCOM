from datetime import date, timedelta
import datetime

def GetDate(birthday):
    if birthday[4][10:] == "Alive":
        return (birthday[3][15:])
    else:
        pass
        
def UpcomingBirthday(IndList,wr):
    wr.write("\n\nUS38  - Upcoming Birthdays\n")
    now = date.today()
    then = now + timedelta(days=30)
    monthdays = []
    while now <= then:
        monthdays = monthdays + ["{}-{:02d}".format(now.month,now.day)]
        now += timedelta(days=1)
    count = 0
    DOB = []
    for ind in IndList:
        if GetDate(ind) in monthdays and int(now.year) > int(ind[3][10:14]):
            DOB = DOB + [ind[3][10:]]
            count += 1
        else:
            continue             
    if count == 0:
        wr.write ("No upcoming birthdays")
    else:
        output = str(count) + " upcoming birthdays " + str(DOB)
        wr.write(output)