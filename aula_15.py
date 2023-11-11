# Exercício 1: Calcule a raiz quadrada de um número inteiro inserido pelo usuário usando o módulo math

import math

numero = int(input("Escreva um numero:\n"))
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)

# Exercício 2: Calcule o valor absoluto de um número decimal inserido pelo usuário usando o módulo math

numero_decimal = float(input("Escreva um numero:\n"))
valor_absoluto = math.fabs(numero_decimal)
print(valor_absoluto)

# Exercício 3: Arredonde um número decimal inserido pelo usuário para o inteiro mais próximo usando o módulo math

numero_decimal1 = float(input("Escreva um numero:\n"))
arredondar = math.ceil(numero_decimal1)
print(arredondar)

# Exercício 4: Calcule o seno de um ângulo em graus inserido pelo usuário usando o módulo math.

angulo = int(input("Escreva um numero:\n"))
seno = math.sin(angulo)
print(seno)

# **`DESAFIO:`** 
# CRIE UM MÓDULO QUE SEJA CAPAZ DE FAZER A OPERAÇÃO DE UM BANCO
# A PRINCIPIO APENAS SAQUES E DEPOSITO

def banco (deposito,saque):
    deposito = (f"colocar dinheiro {deposito}")
    saque = (f"retirar dinheiro {saque}")
valor_inicial = 700
dinheiro = int(input("Digite um valor:\n"))
operacao = str(input("Digite qual operação você deseja realizar:\n"))
saque = int(valor_inicial - dinheiro)
deposito = int(valor_inicial + dinheiro)
if operacao == "saque":
   saldo = (saque) 
   print(f"seu saldo é: R${saldo}")
else:
   saldo = (deposito) 
   print(f"seu saldo é {saldo}")

# OUTRO EXEMPLO DE BANCO 
menu.py

def menu():
    print(''' 
          
          1 - para saque
          2 - para deposito
          3 - Verificar         
          
          
          
          ''')


# -------------------------------------------------------

deposito.py

def deposito(a,b):
    print(a+b)


# ---------------------------------------------------------
saque.py

def saque(a,b):
    print(a-b)

# -----------------------------------------------------------
main.py

from deposito import deposito
from saque import saque 
from menu import menu 


menu()
value = 100
def operation():
   
    choose = input('Digite a operação:')
    
    if choose == '1':
       meu_saque= float (input('digite o valor: '))
       print('Valor em conta R$')
       saque(value,meu_saque)
    elif choose == '2':
       meu_deposito= float (input('digite o valor: '))
       print('Valor em conta R$')
       deposito(value, meu_deposito)
    else: 
        print('Escolha uma opção valida')
        operation()          


operation()

def loop():
    choose2 = input('Deseja continuar? S/N')
    print(choose2)
    while choose2 == 'S': 
          operation()       
        
loop()

#FORMAS DE IMPORTAR BIBLIOTECAS
import math as matematica #renomear a biblioteca
import math #importa tudo de dentro da biblioteca 
from math import calcular #importa uma certa coisa de dentro da variável

