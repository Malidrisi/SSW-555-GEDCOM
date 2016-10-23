def correctgender(FamList,IndList,wr):
    wr.write("\n\nUS21  - Correct gender for role")
    flag = False
    def getsex():
        for person in IndList:
            if person[0] == i[1]:
                return person[2][4:] 
    def getname():
        for person in IndList:
            if person[0] == i[1]:
                return person[1][5:]
    Hus = []
    Wife = []
    for Fam in FamList:
        for item in Fam:
            i = item.split()
            if i[0] == "HUSB":
                husName = getname()
                husSex = getsex()
                if husSex == "M":
                    continue
                else:
                    Hus = Hus + [husName] + [husSex]
                    flag = True
            if i[0] == "WIFE":
                wifeName = getname()
                wifeSex = getsex()
                if wifeSex == "F":
                    continue
                else:
                    Wife = Wife + [wifeName] + [wifeSex]
                    flag = True
    if flag == False:
        wr.write("\nAll gender are correct")
    else:
        output = "\n" + str(Hus) + " is incorrect gender, Husband has to be male"
        wr.write(output)
        output2 = "\n" + str(Wife) + " is incorrect gender, Wife has to be female"
        wr.write(output2)