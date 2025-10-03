print("Menu Calculadora")
print("Escolha o operador aritimético")
type_operator = int(input(f" Digite 1 para Soma \n Digite 2 para Subtração \n Digite 3 para Multiplicação \n Digite 4 para Divisão \n "))

if type_operator == 1:
    print("Menu Soma")
    num1 = int(input(f"Digite o primeiro numero: "))
    num2 = int(input(f"Digite o segundo numero: "))
    resultado = print(f"O resultado da soma de {num1} + {num2} é: {num1 + num2}")
elif type_operator == 2:
    print("Menu Subtração")
    num1 = int(input(f"Digite o primeiro numero: "))
    num2 = int(input(f"Digite o segundo numero: "))
    resultado = print(f"O resultado da subtração de {num1} - {num2} é: {num1 - num2}")
elif type_operator == 3:
    print("Menu Multiplicação")
    num1 = int(input(f"Digite o primeiro numero: "))
    num2 = int(input(f"Digite o segundo numero: "))
    resultado = print(f"O resultado da multiplicação de {num1} multiplicado por {num2} é: {num1 * num2}")