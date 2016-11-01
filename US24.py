
def GetName(ID,IndList):
    for ind in IndList:
        if ind[0] == ID:
            name= ind[1].split()
            return name[1]
def UniqueFamiliesBySpouses(IndList,FamList,wr):
    wr.write("\n\nUS24 - Unique families by spouses")
    UniFam=[]
    for Fam in FamList:
        FamSM=[] 
        for i in range(len(Fam)):
            if (Fam[i][0:9]) == "MARR Date":
                FamSM= FamSM + [GetName(Fam[1][5:],IndList)]+ [Fam[i][10:]]
        if FamSM in UniFam:
            output= "\nERROR: a family with the same husband name and marriage date already exists " + str(FamSM)
            wr.write(str(output))
        else:
            UniFam= UniFam+[FamSM]