import sys

f1 = open('Project01-SaloniSetia.ged')
orig_stdout = sys.stdout
f2 = open('output.txt', 'w')
sys.stdout = f2
tag_list1 = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV','HEAD','TRLR']
tag_list2 = ['INDI','FAM']
for line in iter(f1):
    print ('\n' + line)
    words = line.split()
    if words[0] == 'NOTE:':
        pass
    elif words[1] == 'DATE' and words[0] == '2':
        print (words[0])
        print (words[1])
    elif words[1] in tag_list1:
        print (words[0])
        print (words[1])
    elif len(words) > 2 and words[2] in tag_list2:
        print (words[0])
        print (words[2])
    else:
        print (words[0])
        print ('Invalid Tag')
sys.stdout = orig_stdout
f1.close()
f2.close()