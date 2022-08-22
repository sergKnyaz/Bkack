
print(divmod(38,11))                # Пара (x // y, x % y)
print(abs(-45))                     # Модуль числа

    # Ситуации, где полезно использовать словарь Python (подсчет знаков в тексте)
    # 1 подсчет количества объектов
s='input() fools'
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in sorted(d):
    print(i,d[i], end='\t')
print()
    

  # Второй вариант(тоже самое только через git)

s='input() fools'
d={}
d={}
for i in s:
    if i.isalpha():              # только буквы
        d[i]=d.get(i,0) +1
for i in sorted(d):
    print(i,d[i], end='\t')
print()
    

      # 2 замена заряженного списка( список в котором много нулей(s=[0,0,3,0,6,0,0,0,5,]))
      # было

s='input() fools'
d={}
leters=[0]*26
for i in s.lower():
    if i.isalpha():
        nomer=ord(i)-96
        leters[nomer]+=1

for i in range(26):
    # if leters[i]>0:
        print(chr(i+97), leters[i], end='\t')        # заменняем на предыдущий вариант и он занимает меньше памяти
print()


        # Установить соответствие между объектами(сам составляю переводчик)

words={}
while True:
    s=input()
    if s in words:
        print(s,'=\t', words[s])
    else:
        print('Ведите перевод слова',s)
        transllate=input()
        words[s]=transllate.upper()


        # хранение данных в объекте

contacts={
    'Сергей': {
        'день рождения': '5.11.1984', 'город':'питер',
        'телефон':'8 905 252 73 65','детей': 1
    },
    'Катя': {
        'день рождения': '28.07.1988', 'город':'вологда',
        'телефон':'8 953 502 50 24','детей': 2
    },
    'Михаил': {
        'день рождения': '20.06.2016', 'город':'вологда',
        'телефон':'нет','детей': 'сам еще ребенок'
    }
}

persons=['Сергей','Катя','Михаил']

#   1
for i in persons:
    print('1',i)

#   2
for i in persons:
    print('2',i, contacts[i])

#   3
for i in persons:
    print('3',i, contacts[i]['день рождения'])

#   4
for i in persons:
    print('\n4',i, end=' - ')
    for data in contacts[i]:
        print(data, end=', ')

#   5
for i in persons:
    print('\n5',i)
    for data in contacts[i]:
        print(data, contacts[i][data])
        