def ListDeceased(IndList):
    for Ind in IndList:
        if Ind[4][10:] == "Alive":
            pass
        else:
            print "US29 - List deceased"
            print Ind[0], Ind[1][5:], "died in", Ind[4][10:]
            