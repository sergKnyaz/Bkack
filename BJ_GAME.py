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
    """Игра
    syill_playing - Возвращает игроков оставшихся в игре(не перебравших очков)
    __additional_cards - Сдает дополнительные карты игрокам и диллеру
    """

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name+'\t')
            self.players.append(player)
        self.dealer = BJ_Dealer('Диллер\t')
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def playe(self):
        # Сдача по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()  # переворачиваем карту диллера рубашкой вверх
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lost()
                    else:
                        player.push()
        for player in self.players:
            player.cler()
        self.dealer.cler()


def main():
    print('Добро пожаловать в Блэк Джек')
    names = []
    number = games.ask_number('Сколько играков будет играть? 0т 1 до 7  ', low=1, high=7)
    for i in range(number):
        name = input('Введите ваше имя: ')
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != 'n':
        game.playe()
        again = games.ask_yes_no('Хотите ещё партию? y/n   ')
        main()


main()
