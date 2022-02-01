import random
import string

inteiro = random.randint(0, 85)
decimal = random.uniform(5, 16)
print(inteiro, "|", decimal)
flutuante = random.random()  # gera um float aleatorio entre 0 e 1
print(flutuante)
print(45 * "-")
randomico = random.randrange(100, 1000, 20)
print(randomico)
print(45 * "-")
lista = ["nome1", "nome2", "nome3", "nome4", "nome5"]
sorteio = random.sample(lista, 2)  # gera mais de um aleatorio sem repetir
print(sorteio)
sorteio = random.choice(lista)  # gera 1 aleatorio
print(sorteio)
random.shuffle(lista)  # embarralha a lista
print(lista)
print(45 * "-")
# gerador de senha aletorio
letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%&*.-_"
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=12))
print(senha)
