tagsL0A = ['HEAD','TRLR','NOTE']
tagsL0B = ['INDI','FAM']
tagsL1 = ['NAME','SEX','BIRT','DEAT','FAMC','FAMS','MARR','HUSB','WIFE','CHIL','DIV']
tagsL2 = ['DATE']

myfile = open('/Users/Mahalidrisi/Desktop/STEVENS/555/HW/Homework01-Maha.ged', 'r')
for l in myfile:
    print "The line is: ", l
    print "The level number is: ",l[0],"\n"
    words= l.split()
    
    if l[0] == '0':
        if words[1].strip()  in tagsL0A :
            print "The tag is: ",words[1].strip(),"\n\n"
        elif words[2].strip() in tagsL0B :
            print "The tag is: ",words[2].strip(),"\n\n"
        else: 
            print "invalid tag", "\n\n"   
                        
    elif l[0] == '1':                  
        if words[1].strip()  in tagsL1 :
            print "The tag is: ",words[1].strip() ,"\n\n"
        else:
            print "invalid tag", "\n\n"
            
    elif l[0] == '2':                  
        if words[1].strip() in tagsL2 :
            print "The tag is: ",words[1].strip(),"\n\n"
        else:
            print "invalid tag", "\n\n"
            
    else: 
        print "invalid tag", "\n\n"
                    