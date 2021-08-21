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
            value = BJ_Cards.index(self.rang) + 1
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
                self.cards.append(rang, suit)


class BG_Hand(object):
    """Рука- набор карт на руках игрока
    name - имя игрока
    total - кол-во очков на руках игрока
    """


class BJ_Player(BG_Hand):
    """Игрок"""


class BJ_Dealer(BG_Hand):
    """Диллер"""


class BJ_Game(object):
    """Игра"""
