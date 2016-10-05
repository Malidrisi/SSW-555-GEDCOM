def ListDeceased(IndList,flag,wr):
    dead =0
    wr.write("\n\nUS29 - List deceased")

    for Ind in IndList:        
        if Ind[4][10:] == "Alive":
            pass
        else:
            dead = dead +1 
            if flag == 1:
                output= "\n" + Ind[0] + "\t" +Ind[1][5:] + "\t"+ "died in " +Ind[4][10:]
                wr.write(str(output))
   
    if dead == 0:
        if flag == 1:
            wr.write("\nAll Indviduals are alive")
        else:
            return "All Indviduals are alive"
    elif flag == 0:
        return dead