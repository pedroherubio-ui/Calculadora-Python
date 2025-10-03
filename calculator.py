print("Menu Calculadora")
print("Escolha o operador aritimético")
try:
    type_operator = int(input(f" Digite 1 para Soma \n Digite 2 para Subtração \n Digite 3 para Multiplicação \n Digite 4 para Divisão \n "))
    if type_operator not in [1, 2 ,3 ,4]:
        print("Numero invalido")
    else:
        try: 
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))

            if type_operator == 1:
                print("Menu Soma")
                resultado = num1 + num2
                print(f"O resultado da soma de {num1} + {num2} é: {resultado}")
            elif type_operator == 2:
                print("Menu Subtração")
                resultado = num1 - num2
                print(f"O resultado da subtração de {num1} - {num2} é: {resultado}")
            elif type_operator == 3:
                print("Menu Multiplicação")
                resultado = num1 * num2
                print(f"O resultado da multiplicação de {num1} multiplicado por {num2} é: {resultado}")
            elif type_operator == 4:
                try:    
                    print("Menu Divisão")
                    resultado = num1 / num2
                    print(f"O resultado da divisão de {num1} divido por {num2} é: {resultado}")
                except ZeroDivisionError:
                    print("Não é possivel dividir o numero zero")
        except ValueError: 
                print("Digite apenas numeros válidos")
except ValueError:
    print("Erro: Digite apenas números válidos para escolher a operação.")