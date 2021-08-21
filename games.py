class Players(object):
    """Участники игры"""

    def __init__(self, player, score=0):
        self.player = player
        self.score = score

    def __str__(self):
        rep = self.player + ':\t' + str(self.score)
        return rep


def ask_yes_no(question):
    """Возващает да или нет на вопрос"""
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Возвращает число в пределах low,high"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
if __name__=='__main__':
    print('Модуль вызван на прямую')
    input('Нажмите ENTER,что бы выйти')