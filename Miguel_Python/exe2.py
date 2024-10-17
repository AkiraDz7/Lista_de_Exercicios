numero = int(input("Insira um número: "))
numero2 = int(input("Insira um número: "))
operador = str(input("insira um operador numerico: "))
if (operador == '+'):
    soma = numero + numero2
    print(soma)
elif (operador == '*'):
    multiplicador = numero * numero2
    print(multiplicador)
elif (operador == '/'):
    divisao = numero / numero2
    print(divisao)
elif (operador == '-'):
    menos = numero - numero2
    print(menos)

