
import random

mlist=["EMRE","HATEM","MUHAMMED","GÖKHAN","CENGİZ","CUMAALİ","NAZLI"]
guys=[]
for i in range(len(mlist)) :
    a=random.choice(mlist)
    guys.append(a)
    mlist.remove(a)
    
harf=["A","B","C","D","E","F"]
l1=[]
final=[]
print("First tour matches")
print("")

for i in range (len(guys)):
    if len(guys)<4:
        break
    count=0
    print(harf[i],"grubu")
    for j in range (len(guys)):
        j=0
       

        l1.append(guys[j])
        guys.remove(guys[j])
        count=count+1
        
        if count==4:
            print(l1[0],"and",l1[1])
            print(l1[2],"and",l1[3])
            l1=[]
            print("")
            break
            
if len(guys)==3:
    t1=random.choice(guys)
    guys.remove(t1)
    print(harf[i],". group")
    i=i+1
    print(guys[0],"and",guys[1])
    print("")
    print("got through to upper tour:",t1)
    final.append(t1)
    print("")
    print("")
    
elif len(guys)==2:
    print(harf[i],". group")
    i=i+1
    print(guys[0],"ve",guys[1])
    print("")
    print("")
elif len(guys)==1:
    print("got through to upper tour :",guys[0]) 
    final.append(guys[0])
    print("")
    print("")
   
a=i


print("FINAL TOUR EVENTS")
print("")


finalist=["A GROUP WINNER","B GROUP WINNER","C GROUP WINNER","D GROUP WINNER","E GROUP WINNER","F GROUP WINNER"]
for i in range (a):
    final.append(finalist[i])



newlist=[]
a=len(final)
if len(final)==4:
    print("semi final:")
elif len(final)==2:
    print("final:")

for i in range(a) :
    try:
        x=random.choice(final)
        final.remove(x)
    except:
        break
    try:
        y=random.choice(final)
        final.remove(y)
        print(x,"and",y)
    except:
        print("")
        print("got through to upper tour:",x)
        
