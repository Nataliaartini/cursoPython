#com _ antes eu torno ele protected mas ainda consigo acessar, colocando _e o inicio do nome
#com __ antes eu torno ele private, isso proibe o acesso ao atributo ou método
#até consigo acessar e modificar mas apenas fora da classe dessa maneira _NomeClasse__NomeAtributo

class DataBase:
    def __init__(self):
        self.__dados = {}  # isso aqui é muito importante pro meu código, qualquer alteração pode quebrar ele todu

    def insere_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def imprime_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]


base = DataBase()
base.insere_cliente(1, "protásio")
base.insere_cliente(2, "magno")
base.insere_cliente(3, "barão")
base.apaga_cliente(3)

base.__dados = "outra coisa"
print(base.__dados) #quando eu coloquei o __ python renomeou meu atributo
print(base._DataBase__dados)
base.imprime_clientes()
