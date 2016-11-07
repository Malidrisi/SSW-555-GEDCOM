def MarriageBeforeDivorce(IndList,FamList,wr):
    wr.write("\n\nUS04 - Marriage Before Divorce\n")
    Flag = False
    def getDates(FamList):
        list = []
        for index in range(len(FamList)):
            for data in range(len(FamList[index])):
                if  "HUSB" in FamList[index][data]:
                    list = [FamList[index][data]]+[FamList[index][data+1]]
                if  "MARR" in FamList[index][data]:
                    list = list + [FamList[index][data]]+[FamList[index][data+1]]
                    return list
    for ind in IndList:
        Dates = getDates(FamList)
        if Dates[0][5:] == ind[0]:
            husName = ind[1][5:]
        if Dates[1][5:] == ind[0]:
            wifeName = ind[1][5:]
    if Dates[2][10:] > Dates[3][9:]:
        pass
    else:
        wr.write ("Marriage of " + husName + " and " + wifeName + " occurs after their divorce date")
        Flag = True
    if Flag == False:
        wr.write ("All marriage dates occur before divorce") 