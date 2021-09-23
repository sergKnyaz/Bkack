import cards, games,combinar

class P_Cart(cards.Card):
    @property
    def rang_value(self):
        r=P_Cart.RANKS.index(self.rang)+1
        if r==1:r=14
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

class P_Table(cards.Hand):
    '''набор карт на руках игрока'''
    def __init__(self,name):
        super().__init__()
        self.name=name

    def __str__(self):
        rep=self.name+':  '+super().__str__()
        return rep

class P_Hand(cards.Hand):
    '''набор карт на руках игрока'''
    def __init__(self,name,table):
        super().__init__()
        self.table=table
        self.name=name
    
    def __str__(self):
        rep=self.name+':  '+super().__str__()
    
        rep+='('+str(self.total_rang)+')'
        return rep
   
    @property
    def total_rang(self):
        total=[[],[]]
        for card in self.cards:
            total[0].append(card.rang_value)
        for car in self.table:
            total[0].append(car.rang_value)
        for card in self.cards:
            total[1].append(card.suit_value)
        for car in self.table:
            total[1].append(car.suit_value)
        rezul=combinar.Sov_Rang(total)
        return rezul.total_ran()

# None
class P_Playr(P_Hand):
    
    def win(self):
        print(self.name, 'Победил')

    def pass_con():
        repronse=games.ask_yes_no('играем или пас')
        return repronse=='y'

class P_Game():

    def __init__(self,names):
        self.players=[]
        self.table=P_Table("на столе")
        for name in names:
            player=P_Playr(name,self.table.cards)
            self.players.append(player)
        self.deck=P_Deck()
        self.deck.populate()
        self.deck.shuffle()
    
    # None
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
       

def main():
    print('добро пожаловать в игру Poker')
    names=['Жорик','Бородач','Равшан','Джумшут','Вася']
    # numbers=games.ask_number('сколько играков будет играть?   ',low=2,high=6)
    # for i in range(numbers):
    #     name=input('Введите имя   ')
    #     names.append(name)
    print()
    game=P_Game(names)
    alain=None
    while alain!='n':
        game.playe()
        alain=games.ask_yes_no('Ещё партию?   ')
        main()
    input('exit')

main()