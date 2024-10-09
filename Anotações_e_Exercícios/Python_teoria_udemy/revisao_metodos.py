class Conection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #setter -> mudam o estado dos atributos
        self.user = user

    def set_password(self, password): #setter -> mudam o estado dos atributos
        self.password = password

    @classmethod
    def create_with_auth(cls, user, passsword):
        conexao = cls()
        conexao.user = user #define os atributos do cls aqui para não confundi!
        conexao.password = passsword
        return conexao
    
    @staticmethod
    def log(msg):
        print('LOG', msg)


p1 = Conection()
p1.set_user('Letícia')
p1.set_password('12234')
print(p1.password)
print(p1.user)
print(vars(p1))

p2 = Conection.create_with_auth('Arthur', '130124')
print(p2.user)
print(p2.password)
print(vars(p2))
print(p2.log('One piece is realllll'))


