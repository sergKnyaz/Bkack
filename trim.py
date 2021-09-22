def qsort(sp):
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
        return qsort(sp1)+sp2+qsort(sp3)
    else:
        return sp

class Sov_Rang():

    def __init__(self,sp_kart):
        self.sp_kart=sp_kart

    def gih(self):
        max=0
        r=0
        for i in self.sp_kart:
            p=i
            ret=0
            for j in self.sp_kart:
                if p==j:
                    ret+=1
            if max<ret:
                max=ret
                r=p
            elif max==ret:
                if r<p:r=p
        if max==1:max=0
        dyr=[max,r]
        return dyr
            
    
   
a=Sov_Rang([2,1])
print(a.gih())


#print(qsort([23,12]))