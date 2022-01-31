class A:
    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_jaexiste"):
            cls._jaexiste = object.__new__(cls)

        def cumprimento(*args, **kwargs):
            print("Olá Terráqueo")

        cls.cumprimento = cumprimento
        cls.nome = "NATALIA"
        return super().__new__(cls)

    def __init__(self):
        print("inicio")

    def __call__(self, *args, **kwargs):
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

    def __setattr__(self, key, value):
        self.__dict__[key] = value  # precisa dessa linha pra definir o parametro nome ali em baixo
        print(key, value)

    def __del__(self):
        print("objeto coletado.")

    def __str__(self):
        return "classe A em str"

    def __len__(self):
        return 55


a = A()
var = a(1, 2, 3, 4, 5, 6, 7)
print(var)
a.cumprimento()
print(a.nome) #definido em def new
print(a)  # imprime o def str
print(len(a))
