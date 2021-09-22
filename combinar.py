
a=[[1,5,3,2,5,7,6],[1,3,1,3,2,4,4]] # пара
b=[[1,3,2,2,1,3,6],[1,3,1,3,2,4,4]] #2 пары
c=[[3,4,3,7,3,1,6],[1,3,1,3,2,4,4]] # тройка
d=[[5,3,4,1,2,9,8],[1,3,1,3,2,4,4]] #strit
e=[[1,3,2,2,1,3,6],[3,3,3,2,3,2,3]] #flesh
f=[[1,2,1,2,1,3,4],[1,3,1,3,2,4,4]] #fulhaus
g=[[1,4,1,4,4,4,1],[2,3,4,1,2,3,4]]
h=[[8,9,4,7,10,6,3],[1,3,1,3,1,1,1]] #strit flesh
i=[[14,13,12,4,10,11,2],[3,3,3,2,3,1,3]]  #flesh royal


class Sov_Rang():

    def __init__(self,sp_kart):
        self.sp_kart=sp_kart

    def qsort(self,sp):
        '''СОРТИРОВКА'''
        if len(sp)==2:
            if (sp[0]>sp[1]):
                sp[0],sp[1]=sp[1],sp[0]
            return sp
        elif len(sp)>2:
            sr=sum(sp)//len(sp)
            sp1=[]
            sp2=[]
            sp3=[]
            for i in sp:
                if i<sr:
                    sp1.append(i)
                elif i>sr:
                    sp3.append(i)
                else:
                    sp2.append(i)
            return self.qsort(sp1)+sp2+self.qsort(sp3)
        else:
            return sp

    def gih(self,sps):
        max=0
        r=0
        for i in sps:
            p=i
            ret=0
            for j in sps:
                if p==j:
                    ret+=1
            if max<ret:
                max=ret
                q=r
                r=p
                dir2=[max,r]
            elif max==ret:
                if r<p:
                    q=r
                    r=p
                    dir2=[max,q]
        if max==1:max=0
        dyr=[max,r]
        return dyr,dir2

    def poporyadku(self,sps):
        r=0
        rez=0
        for i in range(len(sps)):
            if (sps[i-1]==(sps[i]-1)):
                r+=1
                if r>3:
                    if sps[-1]==14:rez=1
                    else: rez=2

            elif sps[i-1]!=sps[i]:r=0
        
        return rez


    def total_rang(self):
        '''пара-1, две пары-2, тройка-3, каре-7'''
        sort_rang=self.qsort(self.sp_kart[0])
        sort_suit=self.qsort(self.sp_kart[1])
        print(sort_rang,sort_suit)
        sovp_rang=self.gih(sort_rang)
        sovp_suit=self.gih(sort_suit)
        print(sovp_rang,sovp_suit)
        
        #flesh royal
        if self.poporyadku(sort_rang)==1 and sovp_suit[0][0]>3:
            print('flash royal')
        elif self.poporyadku(sort_rang)==2 and sovp_suit[0][0]>3:
            print('flash strit')




para=Sov_Rang(a)
para.total_rang()
print()
tupara=Sov_Rang(b)
tupara.total_rang()
print()
troic=Sov_Rang(c)
troic.total_rang()
print()
strit=Sov_Rang(d)
strit.total_rang()
print()
flash=Sov_Rang(e)
flash.total_rang()
print()
fulhaus=Sov_Rang(f)
fulhaus.total_rang()
print()
kare=Sov_Rang(g)
kare.total_rang()
print()
strit_flash=Sov_Rang(h)
strit_flash.total_rang()
print()
flash_royal=Sov_Rang(i)
flash_royal.total_rang()