class Verification():
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__lenPassword()
        self.__save()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError('слабый пароль')

    def __save(self):
        with open('user.txt', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')


x = Verification('fools', '12345678')

