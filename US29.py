def ListDeceased(IndList,flag):
    dead =0
    for Ind in IndList:        
        if Ind[4][10:] == "Alive":
            pass
        else:
            dead = dead +1 
            if flag == 1:
                print Ind[0], Ind[1][5:], "died in", Ind[4][10:]                
   
    if dead == 0:
        if flag == 1:
            print "All Indviduals are alive"
        else:
            return "All Indviduals are alive"
    elif flag == 0:
        return dead