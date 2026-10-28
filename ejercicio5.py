import math

def periodo(f, x0):
    vistos = {x0: 0}          
    x, i = x0, 0
    while True:
        x = f(x); i += 1
        if x in vistos:
            return i - vistos[x]   
        vistos[x] = i

print("a)", periodo(lambda x: (21*x + 15) % 31, 21))
print("b)", periodo(lambda x: (13*x + 9) % 128, 7))
print("c)", periodo(lambda x: (17*x) % 31, 23))
print("d)", periodo(lambda x: (121 + x) % 256, 17))

estado = (21, 43)
vistos = {estado: 0}
i = 0
while True:
    estado = (estado[1], (21*estado[1] + 15*estado[0]) % 64)
    i += 1
    if estado in vistos:
        print("e)", i - vistos[estado])
        break
    vistos[estado] = i