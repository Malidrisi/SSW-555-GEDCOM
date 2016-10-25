def livingMarried(IndList, FamList, wr):
    husbName = []
    wifeName = []
    wr.write("\n\nUS30 - List Living Married\n")
    for fam in FamList:
        for i in range(len(fam)):
            if (fam[i][0:4]) == "MARR":
                marrDate = fam[i][10:]
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if Ind[0] == husbId:
                if Ind[4][10:] == "Alive":
                    husbName.append(Ind[1][5:])
            if Ind[0] == wifeId:
                if Ind[4][10:] == "Alive":
                    wifeName.append(Ind[1][5:])
    wr.write("List of living married \n" + str(husbName) + "\n" + str(wifeName))