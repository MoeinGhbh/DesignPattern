class Articles:
    def all_article(self):
        print('print all articles')


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def check_user_password(self):
        if self.username == 'admin' and self.password == 'password':
            return True

def outer(Func):
    def inner():
        username = input('Please enter your username')
        password = input('Please enter your password')
        log = Login(username,password)
        res = log.check_user_password()
        if res:
            Func()
        else:
            print('sorry, you don\'t have access')
    return inner

@outer
def show_all_articles():
    articles = Articles()
    articles.all_article()

show_all_articles()