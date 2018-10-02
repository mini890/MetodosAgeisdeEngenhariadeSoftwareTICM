# ler ficheiro csv
# filename = input("Qual é o nome do ficheiro? ")
filename = "1_CSV_caraterizacao_de_residuos_municipios_LIPOR.csv"
f = open(filename, "r")
lineList = f.readlines()
columnList = lineList[0].strip().split(";")
dataList = []
f.close()
for x in range(1, len(lineList)):
    dataList.append(lineList[x].strip().split(";"))

print(dataList[1][4])

# Qual é o valor de metais em Gondomar?
concelho = "Gondomar"
indiceColuna = columnList.index(concelho)
print(indiceColuna)
materialType = "metais"
found = False
for line in range(len(dataList)):
    for column in [1, 2, 3]:
        if dataList[line][column].lower() == materialType.lower():
            found = True
            break
    if (found):
        break

print("line: ", line, "column: ", column)
print(dataList[line][indiceColuna])
