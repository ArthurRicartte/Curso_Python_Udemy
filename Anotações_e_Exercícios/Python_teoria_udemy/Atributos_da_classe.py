class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Maria Letícia Brito Polari', 18)
#pessoa.ano_atual = 1 --> vai alterar o get_nacimento()
print(p1.get_nascimento())


#teste para __dict__ e vars
print(p1.__dict__)
p1.__dict__['A'] = 'M'
print(vars(p1))
del p1.__dict__['A']
print(vars(p1))
#teste para __dict__ e vars

dados = {'nome': 'Maria Letícia Brito Polari', 'idade': 18}
p2 = Pessoa(**dados)
print(vars(p2))
print(p2.nome)
