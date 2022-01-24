def func(*args, **kwargs):
    args = list(args) #trans. tupla em lista
    #print(args[-1])
    #print(len(args))
    print(args)
    nome = kwargs.get("nome") #melhor usar assim caso eu nao tenha certeza de que essa chave existe
    print(nome) #para args nomeados - ou usa só print- kwargs
    idade = kwargs.get("idade")
    if idade:
        print(idade)
    else:
        print("idade não informada")

lista = [1,2,3]
lista1 = [15,20,30]
func(1,2,3,9,8,7)
func(*lista, 4, 5 ,6)
func(*lista1, *lista, nome="Natalia")

variavel = "qualquer coisa"
def func1(arg): #nesse caso estou usando args para não usar variavel global
    arg = arg.replace("qualquer coisa", "quaisquer coisas")
    return arg
variavel1 = func1(arg = variavel)
print(variavel1)

