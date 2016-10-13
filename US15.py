def fewerThan15Siblings(FamList, wr):
    Flag = False
    wr.write("\n\nUS15 - Fewer than 15 siblings\n")
    for fam in FamList:
        count = 0
        for i in range(len(fam)):
            if (fam[i][0:4]) == "CHIL":
                famID = fam[0]
                count = count + 1
        if count > 15:
            wr.write("Family " + famID + " has more than 15 children! \n")
            Flag = True
        wr.write(str(count) + " siblings in family " + famID + "\n")
    return Flag

        