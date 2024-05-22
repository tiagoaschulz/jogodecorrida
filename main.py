import threading
import time
import random

# Classe para representar um carro
class Carro(threading.Thread):
    def __init__(self, nome, pista):
        super().__init__()
        self.nome = nome
        self.posicao = 0
        self.pista = pista
        self.velocidade = random.randint(1, 3)  # Velocidade aleatória do carro

    def run(self):
        while self.posicao < len(self.pista) - 1:  # Enquanto não chegar ao final da pista
            time.sleep(0.05)  # Ajusta o intervalo de tempo entre cada atualização da posição
            self.posicao += self.velocidade
            print(f'{self.nome} percorreu {self.posicao} metros')
        print(f'{self.nome} chegou ao final!')

# Função para exibir a posição final dos carros de forma aleatória
def exibir_posicao_final_aleatoria(carros):
    carros_ordenados = sorted(carros, key=lambda carro: random.random())  # Embaralha a lista de carros
    print("\nPosição final dos carros:")
    for i, carro in enumerate(carros_ordenados):
        print(f"{i+1}º lugar: {carro.nome}")

# Pista de corrida
pista = ['_' for _ in range(50)]  # Reduz a distância da pista

# Criar os carros
carro1 = Carro('Carro 1', pista)
carro2 = Carro('Carro 2', pista)
carro3 = Carro('Carro 3', pista)

# Iniciar a corrida
carro1.start()
carro2.start()
carro3.start()

# Esperar que os carros terminem a corrida
carro1.join()
carro2.join()
carro3.join()

# Exibir a posição final dos carros de forma aleatória
exibir_posicao_final_aleatoria([carro1, carro2, carro3])