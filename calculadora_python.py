
def soma():
  n1 = 0
  n2 = 0
  n1 = float(input("DIGITE UM NÚMERO:"))
  n2 = float(input("DIGITE UM NÚMERO:"))
  numero = n1 + n2
  print("Resultado: ", numero)

def subtrair():
  n1 = 0
  n2 = 0
  n1 = float(input("DIGITE UM NÚMERO:"))
  n2 = float(input("DIGITE UM NÚMERO:"))
  numero = n1 - n2
  print("Resultado: ", numero)

def dividir():
  n1 = 0
  n2 = 0
  n1 = float(input("DIGITE UM NÚMERO:"))
  n2 = float(input("DIGITE UM NÚMERO:"))
  numero = n1 // n2
  print("Resultado: ", numero)

def multiplicar():
  n1 = 0
  n2 = 0
  n1 = float(input("DIGITE UM NÚMERO:"))
  n2 = float(input("DIGITE UM NÚMERO:"))
  numero = n1 * n2
  print("Resultado: ", numero)

def sair():
  print("CALCULADORA FINALIZADA")

while True:
  print("--------ESCOLHA UMA DAS OPÇÕES ABAIXO--------")
  print()
  print(
    '1 - SOMAR'
    '\n2 - SUBTRAIR'
    '\n3 - DIVIDIR'
    '\n4 - MULTIPLICAR'
    '\n5 - SAIR'  
  )
  menu = int(input("INFORME A OPERAÇÃO DESEJADA: "))
  if menu == 1:
    soma()
  if menu == 2:
    subtrair()
  if menu == 3:
    dividir()
  if menu == 4:
    multiplicar()
  if menu == 0:
    break
