class Card(object):
    '''Класс отвечает за генерацию колоды и ее тасовку
    Suit- c(clubs)- трефыб d(diamonds)-буби, h(hearts)-червы, s(spades)- пики
    '''
    RANGS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUIT = ['-c-', '-d-', '-h-', '-s-']

    def __init__(self, rang, suit):
        self.rang = rang
        self.suit = suit

    def __str__(self):
        rep = self.rang + self.suit
        return rep


class Hand(object):
    '''Рука: набор карт на руках одного игрока.
    clear - очищает список карт на руках
    add - добавляет карту на руки
    give - передает карту
    '''

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = '<Пусто>'
        return rep

    def cler(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, otter_hand):
        self.cards.remove(card)
        otter_hand.add(card)


class Deck(Hand):
    '''Класс колода наследник Hand,
    populate - заполняем колоду
    shuffle - тасуем колоду
    deal - раздача карт
    '''

    def populate(self):
        self.cards = []
        for suit in Card.SUIT:
            for rang in Card.RANGS:
                self.add(Card(rang, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)  #####ЗАПОМНИТЬ

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Карты закончились')




deck = Deck()
deck.populate()
deck.shuffle()
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck.deal(hands, per_hand=17)
print(deck)
print(my_hand)
print(your_hand)
