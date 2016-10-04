from prettytable import PrettyTable
import datetime
from US07 import age_less_than_150
from US29 import ListDeceased
from US01 import get_date
from US27 import get_age


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

<<<<<<< Updated upstream
myfile = open('/Users/Mahalidrisi/Desktop/SSW555/data.ged', 'r')
=======
myfile = open('/Users/rafifarab/Desktop/GEDCOM/data.ged', 'r')
>>>>>>> Stashed changes

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
print IndTable	

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
<<<<<<< Updated upstream
print FamTable, "\n"

#UserStories

#US01
print "US01 - Date before current date"
get_date(IndList)

print "\n"

#US07
print "US07 - Less then 150 years old"
age_less_than_150(IndList,1)

print "\n"

#US27
print "US27 - Include individual ages"
get_age(IndList)

print "\n"

#US29
print "US29 - List deceased"
ListDeceased(IndList,1)




=======
print IndList
>>>>>>> Stashed changes
wr=open('output.txt','w')
wr.write("\nIndividuals\n")
wr.write(str(IndTable))
wr.write("\n\nFamilies\n")
wr.write(str(FamTable))
wr.close()   
