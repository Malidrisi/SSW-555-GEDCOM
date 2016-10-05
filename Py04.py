from prettytable import PrettyTable
import datetime
from US01 import get_date
from US03 import birthBeforeDeath
from US07 import age_less_than_150
from US27 import get_age
from US23 import uniqueIndividuals
from US29 import ListDeceased

tagsL0A = ['HEAD','TRLR','NOTE']
tagsL0B = ['INDI','FAM']
tagsL1 = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV']
tagsL2 = ['DATE']

# list to hold current record         
TempRec = []
# list to store individuals information  
IndList = []
# list to store Family information  
FamList = []

FoundInd = False
FoundFam = False
FoundDate = False

def getname():
    for person in IndList:
        if person[0] == Item[1]:
            return person[1][5:]

myfile = open('data.ged', 'r')

for l in myfile:
	words = l.split()
#find and stor individuals 
	if words[0] == '0' and words[-1] == 'INDI':
	    FoundInd = True
	    if len(TempRec) > 0:
	       if TempRec[0][0] == 'I' :
	           IndList = IndList + [TempRec]
	       elif TempRec[0][0] == 'F':
	           FamList = FamList + [TempRec]
	           FoundFam = False
	    TempRec = [words[1].replace('@','')]
		
	if FoundInd and words[1] == 'NAME':
		TempRec = TempRec + [l[2:].strip().replace('/','')]
		
	elif FoundInd and words[1] == 'SEX':
		TempRec = TempRec + [l[2:].strip()]
	
	elif FoundInd and words[1] in ['BIRT','DEAT']:
		FoundDate = True
		DateType = words[1]

	elif FoundInd and words[1] in ['FAMC','FAMS']:
	        if DateType == 'DEAT':
	            TempRec = TempRec + [l[2:].strip().replace('@','')]	            
	        else:
	            TempRec = TempRec + ["DeatDate: Alive"]
	            TempRec = TempRec + [l[2:].strip().replace('@','')]
	            DateType= 'DEAT'

	
#find and store Families
	if words[0] == '0' and words[-1] == 'FAM':
	    FoundFam = True
	    if len(TempRec) > 0:
	       if TempRec[0][0] == 'I' :
	           IndList = IndList + [TempRec]
	           FoundInd = False
	       elif TempRec[0][0] == 'F':
	           FamList = FamList + [TempRec]
	    TempRec = [words[1].replace('@','')]

	if FoundFam and words[1] in ['HUSB','WIFE','CHIL']:
		TempRec = TempRec + [l[2:].strip().replace('@','')]
		
	elif FoundFam and words[1] in ['DIV', 'MARR']:
		FoundDate = True
		DateType = words[1]
# store Date
		
	if FoundDate and words[1] == 'DATE':
		TempRec = TempRec + [DateType +' Date '+ str(datetime.datetime.strptime(l[7:].strip(), '%d %b %Y').date())]	
		FoundDate = False
		
#store last record
if TempRec[0][0] == 'I':
	IndList = IndList + [TempRec]
elif TempRec[0][0] == 'F':
	FamList = FamList + [TempRec]

# sort Individual list in a table
IndList = sorted(IndList, key = lambda i:int(i[0].replace('I',"")))
IndTable = PrettyTable(['ID', 'Name','SEX','Birth Date','Deat Date'])
for i in IndList:
    IndTable.add_row([i[0], i[1][5:], i[2][4:],i[3][10:],i[4][10:]])
#print IndTable	

# sort family list in a table
FamList = sorted(FamList, key = lambda i:int(i[0].replace('F',"")))
FamTable = PrettyTable(['ID', 'Husband Name','Wife Name'])
for Fam in FamList:
        for i in Fam:
        	Item = i.split()
        	if Item[0] == 'HUSB':
        	    hus= getname()
        	if Item[0] == 'WIFE':
        	    wife= getname()        				
        FamTable.add_row([Fam[0], hus, wife])			 
#print FamTable, "\n"

wr=open('output.txt','w')
wr.write("\nIndividuals\n")
wr.write(str(IndTable))
wr.write("\n\nFamilies\n")
wr.write(str(FamTable))

#UserStories

#US01
get_date(IndList,wr)

#US03
birthBeforeDeath(IndList,wr)

#US07
age_less_than_150(IndList,1,wr)

#US23
uniqueIndividuals(IndList,wr)

#US27
get_age(IndList,wr)

#US29
ListDeceased(IndList,1,wr)

wr.close()