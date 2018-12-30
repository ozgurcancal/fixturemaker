import random

class dart:

    def __init__( self,A=[],B=[],C=[],D=[],E=[],F=[],count=0,guys=[]):
        grup=[A,B,C,D,E,F]
        self.A=A
        self.B=B
        self.C=C
        self.D=D
        self.E=E
        self.F=F
        self.count=count
        self.grup=grup
        self.guys=guys
    
    def ondankucukse(self):
        guys=self.guys
        count=self.count
        grup=self.grup
        b=int(len(guys)/2)
        i=0

        while b+i<len(guys)+1:
            
            x=guys[0+i:b+i]

            for j in x:
                grup[count].append(j)
            
            i=i+b
            count=count+1

        self.count=count


    def karistir(self,X):
      
        mlist=[]
        mlist=X
        guys=[]

        for i in range(len(mlist)) :
            a=random.choice(mlist)
            guys.append(a)
            mlist.remove(a)

        self.guys=guys


    def eslestir(self,X):
        if len(X)>2:
            z=int(len(X)/2)

            for i in range(z) :
                print(i+1,".maç : ",end="")
                print(X[2*i],"  ile  ",X[2*i+1])
        
        else:
           print(X[0],"  ile  ",X[1]) 


        
    def dortartıbir(self): 

        guys=self.guys
        count=self.count
        grup=self.grup
        b=int(len(guys)/4)
        i=0

        while b+i<len(guys)+1:
            
            x=guys[0+i:b+i]

            for j in x:
                grup[count].append(j)
            
            self.grup[count]=grup[count]
            i=i+b
            count=count+1

        self.count=count
        

    def ucartıbir(self): 
        guys=self.guys
        count=self.count
        
        grup=self.grup

        b=int(len(guys)/3)
        i=0
        while b+i<len(guys)+1:
            
            x=guys[0+i:b+i]
            for j in x:
                grup[count].append(j)
            
            i=i+b
            count=count+1

        self.count=count


t=dart()

havuzlist=[]
usttur=[]
final=[]

X=["ÖZGÜR","HATEM","MUHAMMED","CUMAALİ","GÖKHAN","EMRE","CENGİZ"]
t.karistir(X)

guys=t.guys
grup=t.grup

print()

if len(guys)<8:
    t.ondankucukse()
    count=t.count

    if len(guys)%2==1:
        print("direk bir üst tura çıkan: ", guys[len(guys)-1])
        usttur.append(guys[len(guys)-1])

elif len(guys)%4==0 or len(guys)%4==1 :

    t.dortartıbir()
    count=t.count

    if len(guys)%4==1:

        print("dirSek bir üst tura çıkan: ", guys[len(guys)-1])
        usttur.append(guys[len(guys)-1])
        guys.remove(guys[len(guys)-1]) 
      
    
elif len(guys)%3==0 or len(guys)%3==1 :

    t.ucartıbir()
    count=t.count

    if len(guys)%3==1:
        print("direk bir üst tura çıkan: ", guys[len(guys)-1])
        havuzlist.append(guys[len(guys)-1])
        guys.remove(guys[len(guys)-1]) 

else :
    t.ucartıbir()
    
    Y=t.A+t.B+t.C+t.D+t.E+t.F

    for i in Y:
        guys.remove(i)

    grup[t.count]=guys
    count=t.count
    count=count+1

for i in range(count):  
    if len(grup[i])%2!=0:
        a=random.choice(grup[i])
        havuzlist.append(a)
        grup[i].remove(a) 

if len(havuzlist)%2!=0:
    a=random.choice(havuzlist)
    usttur.append(a)
    havuzlist.remove(a) 
    
if len(havuzlist)==1:
    usttur.append(havuzlist[0])
    havuzlist.remove(havuzlist[0]) 

elif len(havuzlist)==2:
    x=havuzlist[0:2]

    for j in x:
        grup[count].append(j) 

    count=count+1
             
elif len(havuzlist)>2:
    b=int(len(havuzlist)/len(grup[0]))
    i=0

    while b+i<len(havuzlist)+1:
        x=havuzlist[0+i:b+i]

        for j in x:
            grup[count].append(j)
     
        i=i+b
        count=count+1


print()
harf=["A","B","C","D","E","F"] 

for i in range(count):
    print("grup",harf[i])
    usttur.append(harf[i])
    t.eslestir(grup[i])
    print()

 print()
print("FİNAL TURU")
print()
print()

if len(usttur)%2!=0:
    p=random.choice(usttur)
    usttur.remove(p)
    final.append(p)
    print("ilk finalist:",p)
    
print()
t.eslestir(usttur)
print()

nlist=["1.maçın galibi","2.maçın galibi","3.maçın galibi","4.maçın galibi","5.maçın galibi","6.maçın galibi"]
mac=[]
z=int(len(usttur)/2)

if z>2:

    for i in range(z):
        mac.append(nlist[i])

    t.karistir(mac)
    c=t.guys

    for i in c:
        final.append(i)
    
    if len(final)==2:
        print("final karşılaşması")
        print(final[0],"  ile  ",final[1])    
 
    if len(final)%2!=0:
        a=random.choice(final)
        final.remove(a)
        print("ilk finalist",a)
    
    else:

        for i in range(int(len(final)/2)) :
            print("yarı final",i+1,". karşılaşma : ",end="")    
            print(final[2*i],"  ile  ",final[2*i+1])
            print()


