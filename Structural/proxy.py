class DB:
    def work(self):
        print('you are admin so you can work with DB')


class proxy:
    _password = 'secret'

    def check_user_password(self, password):
        if self._password == password:
            db = DB()
            db.work()
        else:
            print('sorry you dont have permison to access db')

p = proxy()
p.check_user_password('secret')
p.check_user_password('wrong_password')
