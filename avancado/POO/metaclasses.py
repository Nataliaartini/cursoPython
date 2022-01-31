class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if "attr_classe" in namespace:
            print(f"{name} tentou sobrescrever o atributo attr_classe")
            del namespace["attr_classe"]  # excluindo attr_classe da classe B

        print(namespace)
        if "b_fala" not in namespace:
            print(f"você precisa criar o metodo de fala em {name}")
        else:
            if not callable(namespace["b_fala"]):
                print(f"b_fala precisa ser um metodo, não atributo em {name}")

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

    attr_classe = "valor A"  # para não ser sobrescrito estou tratando na metaclasse


class B(A):
    # b_fala = "olá"
    def b_fala(self):
        print("oi")

    attr_classe = "valor B"


b = B()
b.b_fala()
print(b.attr_classe)

C = type("C", (), {"attr": "olá Mundo!"}) #nome da classe, de quem ela está herdando e o que tem nela.
c = C()
print(c.attr)
print(type(c))
