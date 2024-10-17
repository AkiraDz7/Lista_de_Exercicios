numero = int (input('insira um numero: '))
numero2 = int (input('insira um numero: '))
numero3 = int (input('insira um numero: '))

if numero > numero2 or numero > numero3:
    print(f"O maior entre os tres numero e {numero}")
elif numero2 > numero or numero2 > numero3:
    print(f"o maior entre os três numeros é {numero2}")
else:
    print(f"O maior entre os três numeros {numero3} ")