class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        self.__items[index] = valor

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f"{self.__class__.__name__}({self.__items})"

if __name__ == "__main__":
    lista = MinhaLista()
    lista.add("Natalia")
    lista.add("Natan")

    lista[1] = "Lucas"  # tratado em def setitem

    for valor in lista:
        print(valor) #vai gerar indexError tratado com try except em def next

    print(lista[0]) #not subscriptable tratado em def getitem


