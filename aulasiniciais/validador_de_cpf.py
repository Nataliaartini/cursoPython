cpf = "16899535009"
newcpf = cpf[:9]
reverso = 10
total = 0
for i in range(19):
    if i > 8:
        i -= 9
    total += int(newcpf[i]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            digito = 0
        total = 0
        newcpf += str(digito)
print(newcpf)
if newcpf == cpf:
    print("CPF validado")
else:
    print("CPF inválido")
