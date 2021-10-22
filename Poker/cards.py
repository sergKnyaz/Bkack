class Card(object):
    """Класс отвечает за карты и перевернуты они или нет
    Suit- c(clubs)- трефыб d(diamonds)-буби, h(hearts)-червы, s(spades)- пики
    """
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUIT = ['c', 'd', 'h', 's']

    def __init__(self, rang, suit, face_up=True):
        self.rang = rang
        self.suit = suit
        self.face_up = face_up

    def __str__(self):
        if self.face_up:
            rep = self.rang + self.suit
        else:
            rep = ('XX')
        return rep

    def flip(self):
        self.face_up = not self.face_up


class Hand(object):
    """Рука: набор карт на руках одного игрока.
    возвращает набор карт
    clear - очищает список карт на руках
    add - добавляет карту на руки
    give - передает карту
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + "\t"
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
    """Класс колода наследник Hand,
    populate - заполняем колоду
    shuffle - тасуем колоду
    deal - раздача карт
    """

    def populate(self):
        self.cards = []
        for suit in Card.SUIT:
            for rang in Card.RANKS:
                self.add(Card(rang, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)  # ЗАПОМНИТЬ

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print('Карты закончились')
                    


if __name__ == '__main__':
    print('Этот модуль используется для создания карточных игр')
    input('Нажмите ENTER,что бы выйти')
