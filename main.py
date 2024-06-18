import threading   
import time       
import random      

class Carro(threading.Thread): 
    semaforo = threading.Semaphore(1)

    def __init__(self, nome, pista):
        super().__init__()  
        self.nome = nome 
        self.posicao = 0  
        self.pista = pista  
        self.velocidade = random.randint(1, 3) 

    def run(self):  
        while self.posicao < len(self.pista) - 1:  
            time.sleep(0.05) 
            self.posicao += self.velocidade 

            Carro.semaforo.acquire() 
            try:
                print(f'{self.nome} percorreu {self.posicao} metros') 
            finally:
                Carro.semaforo.release() 

        Carro.semaforo.acquire() 
        try:
            print(f'{self.nome} chegou ao final!')
        finally:
            Carro.semaforo.release() 

def exibir_posicao_final_aleatoria(carros):
    carros_ordenados = sorted(carros, key=lambda carro: random.random()) 
    print("\nPosição final dos carros:")
    for i, carro in enumerate(carros_ordenados):  
        print(f"{i+1}º lugar: {carro.nome}")  

pista = ['_' for _ in range(50)] 

carro1 = Carro('Carro 1', pista)  
carro2 = Carro('Carro 2', pista)  
carro3 = Carro('Carro 3', pista)  

carro1.start()  
carro2.start() 
carro3.start()  

carro1.join() 
carro2.join()  
carro3.join()  

exibir_posicao_final_aleatoria([carro1, carro2, carro3])  