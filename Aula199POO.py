class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa ('Idelcio', 'Rocha')
p2 = Pessoa ('Luciane', 'Carneiro')

print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)