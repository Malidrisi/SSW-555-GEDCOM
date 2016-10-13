import datetime 

def marrBeforeBirth(IndList, FamList, wr):
    Flag = False
    wr.write("\n\nUS02 - Birth before Marriage\n")
    for fam in FamList:
        for i in range(len(fam)):
            if (fam[i][0:4]) == "MARR":
                marrDate = fam[i][10:]
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if Ind[0] == husbId:
                husbBirth = Ind[3][10:]
                husbName = Ind[1][5:]
            if Ind[0] == wifeId:
                wifeBirt = Ind[3][10:]
                wifeName = Ind[1][5:]
        if husbBirth < marrDate and wifeBirt < marrDate:
            pass
        elif husbBirth > marrDate:
            wr.write("Birth of " + husbName + " occurs after his marriage\n")
            Flag = True
        elif wifeBirt > marrDate:
            wr.write("Birth of " + wifeName + " occurs after her marriage\n")
            Flag = True
    if Flag == False:
        Print("All Births Occur Before Marriage!")