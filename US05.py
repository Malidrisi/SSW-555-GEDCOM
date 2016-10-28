import datetime 

def marrBeforeDeath(IndList, FamList, wr):
    Flag = False
    husbliveFlag = True
    wifeliveFlag = True
    wr.write("\n\nUS05 - Marriage before Death\n")
    for fam in FamList:
        for i in range(len(fam)):
            if (fam[i][0:4]) == "MARR":
                marrDate = fam[i][10:]
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if Ind[0] == husbId:
                if Ind[4][10:] == "Alive":
                    continue
                else:
                    husbDeat = Ind[4][10:]
                    husbName = Ind[1][5:]
                    husbliveFlag = False
            if Ind[0] == wifeId:
                if Ind[4][10:] == "Alive":
                    continue
                else:
                    wifeDeat = Ind[4][10:]
                    wifeName = Ind[1][5:]
                    wifeliveFlag = False
    if ((husbliveFlag == True) and (wifeliveFlag == True)):
        wr.write("All married individuals are alive!\n")
    else:
        if ((husbliveFlag == False) and (wifeliveFlag == False)):
            if husbDeat > marrDate and wifeDeat > marrDate:
                pass
            elif husbDeat < wifeDeat:
                if husbDeat < marrDate:
                    wr.write("Death of " + husbName + " occurs before his marriage\n")
                    Flag = True
            elif husbDeat > wifeDeat:
                if wifeDeat < marrDate:
                    wr.write("Death of " + wifeName + " occurs before her marriage\n")
                    Flag = True
        elif ((husbliveFlag == False) and (wifeliveFlag == True)):
            if husbDeat > marrDate:
                pass
            elif husbDeat < marrDate:
                wr.write("Death of " + husbName + " occurs before his marriage\n")
                Flag = True
        elif ((wifeliveFlag == False) and (husbliveFlag == True)):
            if wifeDeat > marrDate:
                pass     
            if wifeDeat < marrDate:
                wr.write("Death of " + wifeName + " occurs before her marriage\n")
                Flag = True         
    if Flag == False:
        wr.write("All Marriages Occur Before Death!")
    return Flag
