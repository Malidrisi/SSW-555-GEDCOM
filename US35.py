from datetime import date
import datetime
def ListRecentBirths(IndList,wr):
    count= 0
    wr.write("\n\nUS35 - List Recent Births")
    for Ind in IndList:
        if 0 <= (date.today() - datetime.datetime.strptime(Ind[3][10:], '%Y-%m-%d').date()).days <= 30:
            count= count + 1 
            output= "\n" + Ind[0] + "\t" +Ind[1][5:] + "\t"+ "was born in " +Ind[3][10:]
            wr.write(str(output))
        else:
            pass
    if count == 0:
        wr.write("\nNo one was born recently")