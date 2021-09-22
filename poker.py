import cards, games,trim

class P_Cart(cards.Card):
    @property
    def rang_value(self):
        r=P_Cart.RANKS.index(self.rang)+1
        if r==1:r=13
        return r
    @property
    def suit_value(self):
        s=P_Cart.SUIT.index(self.suit)
        return s

class P_Deck(cards.Deck):
    '''колода для игры'''
    def populate(self):
        for suit in P_Cart.SUIT:
            for rang in P_Cart.RANKS:
                self.cards.append(P_Cart(rang,suit))

class P_Hand(cards.Hand):
    '''набор карт на руках игрока'''
    def __init__(self,name):
        super().__init__()
        self.name=name
    
    def __str__(self):
        rep=self.name+':  '+super().__str__()
    
        rep+='('+str(self.peredelai)+')'
        return rep
    @property
    def peredelai(self):
        s=trim.Sov_Rang(self.total)
        d=s.gih()
        rep=''
        for t in d:
            if t>1:
                if t==11:t='J'
                elif t==12:t='Q'
                elif t==13:t='K'
                elif t==14:t='A'
                rep+=str(t)+' '
        return rep


    @property
    def total(self):
        total=[]
        for card in self.cards:
            total.append(card.rang_value)
        return total


class P_Playr(P_Hand):
    
    def win(self):
        print(self.name, 'Победил')

    def pass_con():
        repronse=games.ask_yes_no('играем или пас')
        return repronse=='y'

class P_Game():

    def __init__(self,names):
        self.players=[]
        for name in names:
            player=P_Playr(name)
            self.players.append(player)
        self.table=P_Hand("на столе")
        self.deck=P_Deck()
        self.deck.populate()
        self.deck.shuffle()
    @property
    def still_player(self,player):
        sp=[]
        for player in self.players:
           if not player.pass_con():
               sp.append(player)
    
    def playe(self):
        # Сдача по 2 карты
        self.deck.deal(self.players,per_hand=2)
        self.deck.deal([self.table],per_hand=5)
        for player in self.players:
            print(player)
        print(self.table)
        for player in self.players:
            sps=[]
            sps.append(player.total)
            sps+=self.table.total
            print(player.peredelai())

def main():
    print('добро пожаловать в игру Poker')
    names=[]
    numbers=games.ask_number('сколько играков будет играть?   ',low=2,high=6)
    for i in range(numbers):
        name=input('Введите имя   ')
        names.append(name)
        print()
    game=P_Game(names)
    alain=None
    while alain!='n':
        game.playe()
        alain=games.ask_yes_no('Ещё партию?   ')
        main()
    input('exit')

main()