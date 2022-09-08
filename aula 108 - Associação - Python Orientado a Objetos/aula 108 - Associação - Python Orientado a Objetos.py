from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Luisao')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

print(escritor.nome)
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()

