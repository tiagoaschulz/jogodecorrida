import threading   
import time       
import random      

# Classe para representar um carro
class Carro(threading.Thread):  # Define a classe Carro que herda de threading.Thread
    semaforo = threading.Semaphore(1)  # Semáforo com valor inicial 1

    def __init__(self, nome, pista):
        super().__init__()  # Inicializa a thread pai
        self.nome = nome  # Nome do carro
        self.posicao = 0  # Posição inicial do carro
        self.pista = pista  # Pista de corrida
        self.velocidade = random.randint(1, 3)  # Velocidade aleatória do carro

    def run(self):  # Método que define o comportamento da thread
        while self.posicao < len(self.pista) - 1:  # Enquanto não chegar ao final da pista
            time.sleep(0.05)  # Ajusta o intervalo de tempo entre cada atualização da posição
            self.posicao += self.velocidade  # Incrementa a posição do carro

            # Utiliza o semáforo para controlar a impressão
            Carro.semaforo.acquire()  # Adquire o semáforo
            try:
                print(f'{self.nome} percorreu {self.posicao} metros')  # Imprime a posição do carro
            finally:
                Carro.semaforo.release()  # Libera o semáforo

        # Utiliza o semáforo para controlar a impressão
        Carro.semaforo.acquire()  # Adquire o semáforo
        try:
            print(f'{self.nome} chegou ao final!')  # Imprime que o carro chegou ao final
        finally:
            Carro.semaforo.release()  # Libera o semáforo

# Função para exibir a posição final dos carros de forma aleatória
def exibir_posicao_final_aleatoria(carros):
    carros_ordenados = sorted(carros, key=lambda carro: random.random())  # Embaralha a lista de carros
    print("\nPosição final dos carros:")
    for i, carro in enumerate(carros_ordenados):  # Enumera e itera sobre os carros ordenados aleatoriamente
        print(f"{i+1}º lugar: {carro.nome}")  # Imprime a posição final de cada carro

# Pista de corrida
pista = ['_' for _ in range(50)]  # Cria uma lista de 50 underscores representando a pista

# Criar os carros
carro1 = Carro('Carro 1', pista)  # Instancia o carro 1
carro2 = Carro('Carro 2', pista)  # Instancia o carro 2
carro3 = Carro('Carro 3', pista)  # Instancia o carro 3

# Iniciar a corrida
carro1.start()  # Inicia a thread do carro 1
carro2.start()  # Inicia a thread do carro 2
carro3.start()  # Inicia a thread do carro 3

# Esperar que os carros terminem a corrida
carro1.join()  # Espera o término da thread do carro 1
carro2.join()  # Espera o término da thread do carro 2
carro3.join()  # Espera o término da thread do carro 3

# Exibir a posição final dos carros de forma aleatória
exibir_posicao_final_aleatoria([carro1, carro2, carro3])  # Exibe a posição final dos carros em ordem aleatória
