def UniqueIDs(IndList,wr):
    wr.write("\n\nUS22 - Unique IDs")
    Unique = []
    Duplicate = []
    for id in (IndList): 
        if id[0][0] == "I":
            Unique = Unique + [id[0]]
        else:
            pass
    flag = False
    for i in range(0,len(Unique)-1):
        if Unique[i] == Unique[i+1]:
            Duplicate =  Duplicate + [str(Unique[i])]
            flag = True
        else:
            i = i+1       
    if flag == False:
        wr.write ("\nAll IDs are correct")
    else:
        output = "\nError: Duplicate ID for" + str(Duplicate)
        wr.write (output)