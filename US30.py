def livingMarried(IndList, FamList, wr):
    living = []
    wr.write("\n\nUS30 - List Living Married\n")
    for fam in FamList:
        for i in range(len(fam)):
            if (fam[i][0:4]) == "MARR":
                marrDate = fam[i][10:]
                husbId = fam[1][5:]
                wifeId = fam[2][5:]
        for Ind in IndList:
            if ((Ind[0] == husbId) or (Ind[0] == wifeId)):
                if Ind[4][10:] == "Alive":
                    living.append(Ind[1][5:])
    wr.write("List of living married \n" + str(living))