numero = int(input("Insira um número: "))
if numero >= 1:
        for i in range(1, numero):
            if numero % i != 0:
                print(numero, 'é primo')
else:
            print(numero, 'não é primo')