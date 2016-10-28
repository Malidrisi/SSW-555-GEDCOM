from collections import OrderedDict
from operator import itemgetter
import datetime

def orderSiblingsByAge(IndList, FamList, wr):
    child = {}
    wr.write("\n\nUS28 - Order Siblings by Age\n")
    for fam in FamList:
        child.clear()
        for i in range(len(fam)):
            famID = fam[0]
            if (fam[i][0:4]) == "CHIL":
                id = fam[i][5:]
                for Ind in IndList:
                    if Ind[0] == id:
                        my_date = Ind[3][10:].strip()
                        birtDate = datetime.datetime.strptime(my_date,'%Y-%m-%d')
                        Today = datetime.datetime.today()
                        age = (Today - birtDate).days/365
                        if age < 0:
                            child.setdefault(Ind[1][5:], []).append("Invalid")
                        else:
                            child.setdefault(Ind[1][5:], []).append(age)
        wr.write(famID + "\n")
        sortedChildren = OrderedDict(sorted(child.items(), key = itemgetter(1)))
        for key,value in sortedChildren.items():
            wr.write(str(key) + " , Age : " + str(value) + "\n")
        sortedChildren.clear()