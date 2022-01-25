l0 = ["ana", "natalia"]
l1 = [1,2,3,4,5,6]
l2 = [valor for valor in l1]
l3 = [var * 2 for var in l1]
l4 = [(var, var1) for var in l1 for var1 in range(3)]
l5 = [v.replace("a", "@") for v in l0]
print(l2)
print(l3)
print(l4)
print(l5)