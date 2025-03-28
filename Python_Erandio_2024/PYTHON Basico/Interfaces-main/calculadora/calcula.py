# -*- coding: utf-8 -*-

# def suma(num1, num2):
#     return num1 + num2

# def resta(num1, num2):
#     return num1 - num2

# def multiplica(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     return num1/num2

# def porcentaje(num1, num2):
#     return num1 * num2 / 100

operaciones = {"sumar": lambda num1, num2: num1 + num2, 
               "restar": lambda num1, num2: num1-+ num2, 
               "dividir": lambda num1, num2: num1 / num2, 
               "multiplicar": lambda num1, num2: num1 * num2, 
               "porcentaje": lambda num1, num2: (num1 / num2)*100}

def calcula(operando1, operacion, operando2):
    num1 = float(operando1)
    num2 = float(operando2)
    resultado = operaciones[operacion](num1, num2)
    if resultado == int(resultado):
        resultado = int(resultado)
    return str(resultado)[:9]

calcula("24", "sumar", "12")
