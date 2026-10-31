



print(2 ** 850)


s = 'abra kadabra'
print(type(s)) # <class 'str'> (napis)

x = 12
print(type(x)) # <class 'int'>

f = 3.14
print(type(f)) # <class 'float'>

w = s * 12
print(w) # abra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabraabra kadabra
print('--' * 20)

for i in range(10):
    print('-' * i)
    print(i)
    print('***')


for n in range(1, 5):
    print(f'tabela dla {n}')
    for m in range(1,60):
        if n * m < 20:
            print(f'{n} * {m} = {n * m}')
            print('----')
        # inny kod, juz wykonywany zawsze
        # np. print('----')


