class Desk():
    '''Класс отвечает за генерацию колоды и ее тасовку'''
    RANGS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUIT = ['c', 'd', 'h', 's']
    def __init__(self,rang,suit):
        self.rang=rang
        self.suit=suit
    def __str__(self):
        rep=self.rang+self.suit
        return rep
def fool():
    pass

