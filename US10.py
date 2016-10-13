from dateutil.relativedelta import relativedelta
import datetime

def marriageAfter14(IndList, FamList, wr):
    Flag = False
    wr.write("\n\nUS10 - Marriage After 14\n")
    for fam in FamList:
        for i in range(len(fam)):
            if (fam[i][0:4]) == "MARR":
                mDate = fam[i][10:].strip()
                marrDate = datetime.datetime.strptime(mDate,'%Y-%m-%d').date()
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if Ind[0] == husbId:
                date1 = Ind[3][10:].strip()
                husbBirth = datetime.datetime.strptime(date1,'%Y-%m-%d').date()
                husbName = Ind[1][5:]
            if Ind[0] == wifeId:
                date2 = Ind[3][10:].strip()
                wifeBirt = datetime.datetime.strptime(date2,'%Y-%m-%d').date()
                wifeName = Ind[1][5:]
        if husbBirth < marrDate and wifeBirt < marrDate:
            pass
        elif (husbBirth + relativedelta(years=14)) > marrDate:
            wr.write(husbName + " got married before he turned 14\n")
            Flag = True
        elif (wifeBirt + relativedelta(years=14)) > marrDate:
            wr.write(wifeName + " got married before she turned 14\n")
            Flag = True
    if Flag == False:
        Print("All Marriages occured after the individual turned 14!")