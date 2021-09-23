# a=[[1,5,3,2,5,7,6],[1,3,1,3,2,4,4]] # пара
# b=[[1,3,2,2,1,3,6],[1,3,1,3,2,4,4]] #2 пары
# c=[[3,4,3,7,3,1,6],[1,3,1,3,2,4,4]] # тройка
# d=[[5,3,4,1,2,9,8],[1,3,1,3,2,4,4]] #strit
# e=[[1,3,2,2,1,3,6],[3,3,3,2,3,2,3]] #flesh
# f=[[1,2,1,2,1,3,4],[1,3,1,3,2,4,4]] #fulhaus
# g=[[1,4,1,4,4,4,1],[2,3,4,1,2,3,4]]
# h=[[2,3,4,4,5,6,7],[1,3,1,3,1,1,2]] #strit flesh
# i=[[14,13,12,4,10,11,2],[3,3,3,2,3,1,3]]  #flesh royal


class Sov_Rang():
    '''ПРИНИМАЕТ ДВУМЕРНЫЙ СПИСОК'''
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
        '''ВОЗВРАЩАЕТ СОВПАДЕНИЯ И ИХ КОЛИЧЕСТВОБ
         ЕСЛИ СОВПАДЕНИИ 2 ТО ВОЗВРАЩАЕТ ОБА'''
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

    def fullhaus(self,sps):
        '''ДЛЯ ФУЛЛ ХАУС'''
        s_sps=self.gih(sps)
        for i in sps:
            if s_sps[0][1] in sps:sps.remove(s_sps[0][1])
        s_sps2=self.gih(sps)
        if s_sps2[0][0]==2:return True
        

    def poporyadku(self,sps):
        '''ДЛЯ ПРОВЕРКИ КАРТ ПО ПОРЯДКУ(1,2,3,4,5) И ТД ВОЗВРАЩАЕТ ПРИ 5 КАРТАХ ПО ПОРЯДКУ'''
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

    def suit_flash(self,sps,sps2):
        if self.poporyadku(sps)>0:
            r=0
            for i in range(len(sps)):
                if (sps[i-1]==(sps[i]-1)):
                    if sps2[i-1]==sps2[i]:
                        r+=1
            return r

                

    def rang_smena_znach(self,d):
        if d==11:d='J'
        elif d==12:d='Q'
        elif d==13:d='K'
        elif d==14:d='A'
        return d

    def total_ran(self):
        '''ПРОВЕРКА НА КОМБИНАЦИИ В ПОКЕРЕ'''
        sort_rang=self.qsort(self.sp_kart[0])
        sort_suit=self.qsort(self.sp_kart[1])
        sovp_rang=self.gih(sort_rang)
        sovp_suit=self.gih(sort_suit)

        combo=''
        #flesh royal
        if self.poporyadku(sort_rang)==1 and self.suit_flash(sort_rang,sort_suit)>3:
            combo+=('---------ФЛЭШ РОЯЛ---')
        # flesh street
        elif self.poporyadku(sort_rang)==2 and self.suit_flash(sort_rang,sort_suit)>3:
            combo+=('---------ФЛЭШ СТРИТ')
        # kare
        elif sovp_rang[0][0]==4:
            d=self.rang_smena_znach(sovp_rang[0][1])
            combo+=('--------КАРЕ НА '+str(d))
        # ful haus
        elif sovp_rang[0][0]==3 and self.fullhaus(sort_rang): combo+=('---Фул хаус---')
        # flesh
        elif sovp_suit[1][0]>4: combo+=('---Флэш---')
        # street
        elif self.poporyadku(sort_rang)>0: combo+=('---Стрит---')
        # dreier
        elif sovp_rang[1][0]==3:
            d=self.rang_smena_znach(sovp_rang[0][1])
            combo+=('Тройка на '+str(d))
        # duppel
        elif sovp_rang[0][0]==2 and sovp_rang[0][1]!=sovp_rang[1][1]:
            d=self.rang_smena_znach(sovp_rang[0][1])
            d2=self.rang_smena_znach(sovp_rang[1][1])
            combo+=('Две пары:  '+str(d)+' и '+str(d2))
        # para
        elif sovp_rang[1][0]==2:
            d=self.rang_smena_znach(sovp_rang[0][1])
            combo+=('Пара на '+str(d))
        elif sovp_rang[1][0]==1:
            d=self.rang_smena_znach(sovp_rang[0][1])
            combo+='Старшая карта  '+ str(d)
        return combo




# para=Sov_Rang(a)
# print(para.total_ran())
# print()
# tupara=Sov_Rang(b)
# tupara.total_ran()
# print()
# troic=Sov_Rang(c)
# troic.total_ran()
# print()
# strit=Sov_Rang(d)
# strit.total_ran()
# print()
# flash=Sov_Rang(e)
# flash.total_ran()
# print()
# fulhaus=Sov_Rang(f)
# fulhaus.total_ran()
# print()
# kare=Sov_Rang(g)
# kare.total_ran()
# print()
# strit_flash=Sov_Rang(h)
# print(strit_flash.total_ran())
#print(strit_flash.suit_flash())
# print()
# flash_royal=Sov_Rang(i)
# print(flash_royal.total_ran())