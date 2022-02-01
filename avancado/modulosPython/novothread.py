import time
from threading import Thread
from threading import Lock

class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__() #init da Thread

    def run(self):
        time.sleep(self.tempo)
        print(self.texto)

t1 = MeuThread("olá Mundo!", 1)
t1.start()

t2 = MeuThread("mamma mia Matiello", 1.8)
t2.start()

t3 = MeuThread("qui diliça", 2.3)
t3.start()

for i in range(0, 31, 5):
    print(i)
    time.sleep(.1)

print(45*"-")
def vai_demorar(texto, tempo):
    time.sleep(tempo)
    print(texto)

t = Thread(target=vai_demorar, args=("oi meu chapa", 8))
t.start() #se usar um join a thread vai bloquear novas ações

for i in range(7):
    print(i)
    time.sleep(.3)

while t.is_alive():
    print("esperando meu chapa.")
    time.sleep(2)

print(45*"-")

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire() #tranca o metodo ate ele terminar de se executar

        if self.estoque < quantidade:
            print("\nsem estoque suficiente")
            self.lock.release() #liberando antes do return pra nao dar loop
            return

        time.sleep(1) #pode gerar venda mesmo sem estoque, tratado com funcao lock

        self.estoque -= quantidade
        print(f"\ncompra efetuada com sucesso de:{quantidade} ingressos. {self.estoque} em estoque.")

        self.lock.release() #libera o metodo, evitando vender ingresso sem ter em estoque

if __name__ == "__main__":
    ingressos = Ingressos(10)

    threads = []
    for i in range(1,12):
        t4 = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t4)

    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for i in threads:
            if t.is_alive():
                executando = True
                break

    print(f"\n\nestoque disponível: {ingressos.estoque}")
