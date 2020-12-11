sinal = "+"
numeros = int(input("Até que numero?: "))+1
with open("codigo.py", "w", encoding="utf-8") as code:
    # Inicio do código a declarar variaveis 
    code.write(f"num1 = input(\"Escolhe o primeiro numero: \")\nnum2 = input(\"Escolhe o segundo numero: \")\nsinal = input(\"Quer somar (+), subtrair (-), multiplicar (*) ou dividir (/)?: \")\nif num2 == \"0\" and sinal == \"/\":\n    print(\"Divisão por zero!\")\n    quit()\n")
    for i in range(0,numeros): # Soma
        for x in range (0, numeros):
            code.write(f"if num1 == \"{i}\" and num2 == \"{x}\" and sinal == \"+\": \n    print(\"{i} + {x} = {i+x}\")\n")
    for i in range(0,numeros): # Subtração
        for x in range (0, numeros):
            code.write(f"if num1 == \"{i}\" and num2 == \"{x}\" and sinal == \"-\": \n    print(\"{i} - {x} = {i-x}\")\n")
    for i in range(0,numeros): # Multiplicação
        for x in range (0, numeros):
            code.write(f"if num1 == \"{i}\" and num2 == \"{x}\" and sinal == \"*\": \n    print(\"{i} * {x} = {i*x}\")\n")
    for i in range(0,numeros): # Divisão
        for x in range (1, numeros):
            code.write(f"if num1 == \"{i}\" and num2 == \"{x}\" and sinal == \"/\": \n    print(\"{i} / {x} = {i/x}\")\n")
    code.write(f"else:\n    print(\"Erro, número fora dos pretendidos, por favor escolha números entre 0 e {numeros}\")")
    code.close()