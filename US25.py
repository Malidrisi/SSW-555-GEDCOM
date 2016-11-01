def GetName(ID,IndList):
    for ind in IndList:
        if ind[0] == ID:
            name= ind[1].split()
            return name[1]
def UniqueFirstNamesInFamilies(IndList,FamList,wr):
    wr.write("\n\nUS25 - Unique First Names In Families")
    for Fam in FamList:
        Names=[]
        Names = Names + [GetName(Fam[1][5:],IndList)]+ [GetName(Fam[2][5:],IndList)]
        for i in range(len(Fam)):
            if (Fam[i][0:4]) == "CHIL":
                Names = Names + [GetName(Fam[i][5:],IndList)]
        if len(Names) == len(set(Names)):
            pass
        else:
            output= "\nFamily " + Fam[0] + " has duplicated names " + str(Names)
            wr.write(str(output))