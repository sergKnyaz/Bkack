    #  примерыЖ

a='hello,{}'.format('vasja')                    #  Подставление одной переменной
print(a)
print()

b='{}, {}'.format('1','2')                      # Подставление двух переменных
b2='{2},{1},{0}'.format('1','2','3')            # Подставление двух переменных с измененным порядком
print(b)
print(b2)
print()

c='hi,{fo} {hi}'.format(fo='fools',hi='hello')  # 
print(c)
print()

sps={'x':'256','y':'981'}                       # Подставление из словаря
d='ass: {x}, {y}'.format(**sps)
print(d)

                                        # СИНТАКСИС ФОРМАТ

print("Units destroyed: {players[0]!r}".format(players = ['1', '2',' 3']))      # преобразование +s(человеческое)(можно без него)  или   +r(внутреннее)
print("Units destroyed: {players[0]!s}".format(players = ['1', '2',' 3']))
print()

print('{:<30}'.format('left aligned'))
print('{:>30}'.format('right aligned'))                                         # Выравнивание текста
print('{:^30}'.format('centered'))
print()

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))           # Число в системе счисления.
