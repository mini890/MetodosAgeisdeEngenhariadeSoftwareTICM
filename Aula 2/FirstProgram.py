# coding:UTF8 - Opcional
a = input("Qual é o valor? ")

x = "Introdução" #Py2 pode pedir encoding

print (a)

#range(total)
#range(inicio, fim)
#range(inicio, fim, quantos)

#input usa string

n = int(input("Quantos números? "))
dados = []
for k in range(n):
    dados.append(int(input("Valor? ")))

print (dados)

#imprimir o maior de n números
#Opção 1
print (max(dados))

#Opção 2
maior = dados[0]

for k in range(1, len(dados)):
    if dados[k] > maior:
        maior = dados[k]

print (maior)

#Imprimir todos os valor
#Forma Normal
for k in range(len(dados)):
    print (dados[k])

#Forma Compacta - Não permite saber a posição
for k in dados:
    print (k)

#Concatnar
x = 12
y = "alpha"
z = y + str(x)

s = "um Dois         três   "

#strings
#lower(), upper(), capitalize(), title()
#strip(), lstrip(), rstrip() -  Tira das pontas
#split(), split("|") - Parte em |
#join(lista)