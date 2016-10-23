from datetime import date
import datetime
def ListRecentDeaths(IndList,wr):
    count= 0
    wr.write("\n\nUS36 - List Recent Deaths")
    for Ind in IndList:        
        if Ind[4][10:] == "Alive":
            pass
        else:
            if (date.today() - datetime.datetime.strptime(Ind[4][10:], '%Y-%m-%d').date()).days <= 30:
                 count= count + 1 
                 output= "\n" + Ind[0] + "\t" +Ind[1][5:] + "\t"+ "died in " +Ind[4][10:]
                 wr.write(str(output))
            else:
                pass
    if count == 0:
        wr.write("\nNo one died recently")