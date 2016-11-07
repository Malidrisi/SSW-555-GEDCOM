def DivorceBeforeDeath(IndList,FamList,wr):
    Flag = False
    wr.write("\n\nUS06 - Divorce Before Death\n")
    Flag = False
    for fam in FamList:
        for Item in range(len(fam)):
            if fam[Item][0:3] == "DIV":
                DivorceDate = fam[Item][9:]
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if Ind[0] == husbId:
                husbDeath = Ind[4][10:]
                husbName = Ind[1][5:]
            if Ind[0] == wifeId:
                wifeDeath = Ind[4][10:]
                wifeName = Ind[1][5:]
    if DivorceDate > husbDeath  and DivorceDate > wifeDeath:
        pass
    else:
        wr.write ("Divorce of " + husbName + " and " + wifeName + " occurs after their death date")
        Flag = True
    if Flag == False:
        wr.write ("\nAll divorce dates occur before death")