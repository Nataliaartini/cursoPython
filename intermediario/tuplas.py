#depois que cria uma tupla ela não pode ser alterada
t1 = (1,2,3,4,5,6) * 2
print(t1[3])
print(t1)
for v in t1:
    print(v)
print(t1[3:])
t2 = "a", "b"
print(t2)
t3 = t1+t2
print(t3)
n1,n2,n3, *_ = t3
print(n3)
t1 = list(t1)
t1[1] = 978
print(f"t1 modificada {t1}")
t1 = tuple(t1) #agora t1 é tupla de novo, sem poder ser alterada
