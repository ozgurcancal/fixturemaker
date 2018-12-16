
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
print("BİRİNCİ TUR KARŞILAŞMALARI")
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
            print(l1[0],"ve",l1[1])
            print(l1[2],"ve",l1[3])
            l1=[]
            print("")
            break
            
if len(guys)==3:
    t1=random.choice(guys)
    guys.remove(t1)
    print(harf[i],"grubu")
    i=i+1
    print(guys[0],"ve",guys[1])
    print("")
    print("bir üst tura çıkan:",t1)
    final.append(t1)
    print("")
    print("")
    
elif len(guys)==2:
    print(harf[i],"grubu")
    i=i+1
    print(guys[0],"ve",guys[1])
    print("")
    print("")
elif len(guys)==1:
    print("bir üst tura çıkan:",guys[0]) 
    final.append(guys[0])
    print("")
    print("")
   
a=i


print("FİNAL TURU KARŞILAŞMALARI")
print("")


finalist=["A GRUBU KAZANANI","B GRUBU KAZANANI","C GRUBU KAZANANI","D GRUBU KAZANANI","E GRUBU KAZANANI","F GRUBU KAZANANI"]
for i in range (a):
    final.append(finalist[i])



newlist=[]
a=len(final)
if len(final)==4:
    print("yarı final:")
elif len(final)==2:
    print("final:")
#count=1
for i in range(a) :
    try:
        x=random.choice(final)
        final.remove(x)
    except:
        break
    try:
        y=random.choice(final)
        final.remove(y)
        print(x,"ve",y)
    except:
        print("")
        print("finale çıkan:",x)
        
     ##ayak koyabilirsin
#    count=count+1
##İKİNCİ FİNALİST???