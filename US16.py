def male_LastName(IndList,wr):
    n=0
    wr.write("\n\nUS16 - Male Last Names\n")
    for ind in IndList:
        if ind[2][4:]=="M":
            n = n+1
            name = ind[1].split()
            output= name[-1] +"\n"
            wr.write(output)
        else:
            pass
    if n == 0:
        wr.write("All individuals are females")