# "Блэк Джек" от 1 до 7 игроков
import games, cards


class BJ_Cards(cards.Card):
    """Карта для игры в BlackJack
    value кол-во очков сопутствуещей карте
    """
    ASE_VALUE = 1

    @property
    def value(self):
        if self.face_up:
            value = BJ_Cards.RANKS.index(self.rang) + 1
            if value > 10:
                value = 10
        else:
            value = None
        return value


class BJ_Deck(cards.Deck):
    """Колода
     Представляет собой набор карт(объектов класса BJ_Cards)
     """

    def populate(self):
        for suit in BJ_Cards.SUIT:
            for rang in BJ_Cards.RANKS:
                self.cards.append(BJ_Cards(rang, suit))


class BG_Hand(cards.Hand):
    """Рука- набор карт на руках игрока
    name - имя игрока
    total - кол-во очков на руках игрока
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + super().__str__()
        if self.total:
            rep += str(self.total)
        return rep

    @property
    def total(self):
        # Если у одной из карт value равно None, то все свойство равно None
        for card in self.cards:
            if not card.value:
                return None
        # суммируем очки туз за 1 очко
        total = 0
        for card in self.cards:
            total += card.value
        # Определяем есть ли туз на руках игрока
        contains_ase = False
        for card in self.cards:
            if card == BJ_Cards.ASE_VALUE:
                contains_ase = True
        # если сумма оков меньше 11 то туз считаем за 11
        if contains_ase and total < 11:
            total += 10
        return total

    def is_busted(self):
        return self.total > 21


class BJ_Player(BG_Hand):
    """Игрок"""

    def is_hitting(self):
        response = games.ask_yes_no('Будешь брать еще карту?  ')
        return response == 'y'

    def bust(self):
        print(self.name, 'Перебрал')
        self.lost()

    def lost(self):
        print(self.name, 'Проиграл')

    def win(self):
        print(self.name, 'Победил')

    def push(self):
        print(self.name, 'Сыграл с компьютером в ничью')


class BJ_Dealer(BG_Hand):
    """Диллер"""

    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, 'Перебрал')

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """Игра"""
