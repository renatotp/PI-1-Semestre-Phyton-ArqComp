'''desenvolver um programa que apresente um menu de opões que permita o usuário escolher entre a conversão de decimal para as bases binário, hexadecimal ou octadecimal.'''


import math

opcao = int(input("(1) Decimal -> Binário\n(2) Decimal -> Octadecimal\n(3) Decimal -> Hexadecimal\nEscolha uma opção acima: "))



if opcao==1:
    decimal = int(input("Degite um valor na base Decimal: "))
    resto=[]

    while decimal!=0:
        x=decimal%2
        resto.append(x)
        decimal=decimal//2 #precisa pegar o valor sem a virgula
               
    for n in resto[::-1]: #Aqui é pra inverter a sequencia da lista e tirar as virgulas e o
        print(n, end="")

if opcao==2:
    decimal = int(input("Degite um valor na base Decimal: "))
    resto=[]

    while decimal>8:
        x=decimal%8
        resto.append(x)
        decimal=decimal//8 #precisa pegar o valor sem a virgula

    resto.append(decimal)     
    for n in resto[::-1]: #Aqui é pra inverter a sequencia da lista e tirar as virgulas e o
        print(n, end="")


if opcao==3:
    decimal = int(input("Degite um valor na base Decimal: "))
    resto=[]

    while decimal>16:
        x=decimal%16
        if x==10:
            x="A"
        elif x==11:
            x="B"
        elif x==12:
            x="C"
        elif x==13:
            x="D"
        elif x==14:
            x="E"
        elif x==15:
            x="F"
        resto.append(x)
        decimal=decimal//16 #precisa pegar o valor sem a virgula

    if decimal==10:
        decimal="A"
    elif decimal==11:
        decimal="B"
    elif decimal==12:
        decimal="C"
    elif decimal==13:
        decimal="D"
    elif decimal==14:
        decimal="E"
    elif decimal==15:
        decimal="F"
    resto.append(decimal)     
    for n in resto[::-1]: #Aqui é pra inverter a sequencia da lista e tirar as virgulas e o
        print(n, end="")
