def tarefa(texto, lista=[]):
    lista.extend(texto)
    return lista


def do_undo(lista_tarefa, redo_list):
    if not lista_tarefa:
        print("sem tarefas ainda")
        return
    ultimo = lista_tarefa.pop(-1)
    redo_list.append(ultimo)


def do_redo(lista_tarefa, redo_list):
    if not redo_list:
        print("nada a refazer")
        return
    ultimo_refaz = redo_list.pop()
    lista_tarefa.append(ultimo_refaz)


def show_list(lista_tarefa):
    if not lista_tarefa:
        print("sem tarefas a fazer.")
        return
    else:
        print(lista_tarefa)


lista_tarefa = []
redo = []
while True:
    a = input("deseja adicionar uma tarefa? [y/n]: ")
    if a == "y":
        lista= tarefa(input("adiciona tarefa: "), lista_tarefa)
    else:
        b = input("deseja desfazer ou refazer (l para listar e sair) a ultima ação? [d/r]: ")
        if b == "d":
            do_undo(lista_tarefa, redo)
        elif b == "r":
            do_redo(lista_tarefa,redo)
        else:
            show_list(lista_tarefa)
            break
