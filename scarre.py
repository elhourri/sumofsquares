n = int(input("Donnez un nombre : "))
s = 0
for i in range(1, n * 2 + 1, 2):
    s=s+(i ** 2)
print("Le résultat est :", s)