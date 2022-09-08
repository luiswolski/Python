from pessoa import Pessoa

p1 = Pessoa('Luis', 22)
p1.comer('maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('frango')
p1.parar_falar()
p1.falar('Astronomia')
print(p1.get_ano_nascimento())

print('-------------------------------------------')

p2 = Pessoa('João', 24)
p2.falar('Interestelar')
p2.comer('bolo')
p2.parar_falar()
p2.comer('bolo')
