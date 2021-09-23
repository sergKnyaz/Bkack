import cards,random
from datetime import datetime as dt
# a=[8,8,1,7,3,9,2,2,5,1,7,7,9,9,6,7,7,6,5,0,5,1,1,1,9,8,4,33,64,0,8,68]
# b=[98,34]
# c=[]
# for i in range(30):
#     w=random.randint(1,6)
#     c.append(w)
# print(c)
# print(trim.qsort(a))
# s=trim.Sov_Rang(a)
# s.gih()
# r=''
# for i in a:
#     r+=str(i)
# print(r)

class Player():
    __LVL,__HEALTH=1,100
    __slots__=['__lvl','__heath','__born']

    def __init__(self):
        self.__lvl=Player.__LVL
        self.__heath=Player.__HEALTH
        self.__born=dt.now()
    
    @property
    def lvl(self):
        return self.__lvl,f'{dt.now()-self.__born}'
    
    @lvl.setter
    def lvl(self,number):
        self.__lvl+=Player.__test_tipe(number)
        if self.__lvl>100:self.__lvl=100

    @staticmethod
    def __test_tipe(value):
        if isinstance(value,int):
            return value
        else:
            raise TabError('введите число')

a=Player()
print(a.lvl)
a.lvl=2
print(a.lvl)
