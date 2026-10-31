
lista = []
for i in range(1, 19):
    if i % 2 == 0:
        lista.append(i)
print(lista)
print(len(lista))


print(8 in lista)   # True lub False
print(7 in lista)   # True lub False



from random import randint, seed
seed(42)  # ustalenie pocztku dla liczb "pseudolosowych"
licences = []
for i in range(15):
    new_one = randint(1,100)
    if new_one in licences:
        print('*')
    licences.append(new_one)

print(licences)
