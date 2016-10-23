import datetime
from datetime import date
def all_living_singles(IndList,wr):
    wr.write("\n\nUS31 - All Living Singles")
    flag = False
    list = []
    def getage(ind):
        if ind[4][10:] == "Alive":
            return ((date.today() - datetime.datetime.strptime(ind[3][10:], '%Y-%m-%d').date()).days/365)
    def getname(ind):
        for name in IndList:
            if name[0] == ind[0]:
                return name[1][5:]
    for ind in IndList:
        if getage(ind) >= 30 and ind[5][:4] == "FAMC":
            name = getname(ind)
            list = list + [name]
            flag = True
        else:
            pass
    if flag == False:
        wr.write("\nNo single individual are over 30")
    else:
        output =  "\nIndividuals who are over 30 and single " + str(list)
        wr.write(output)