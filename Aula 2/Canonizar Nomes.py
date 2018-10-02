#nome = input("Diga o nome? ")
nome = "ALEXandre                valente  da  sousa      "
nomeExcepcao = ["de", "da", "das", "do", "dos", "e"]

listaNomes = nome.title().split()
for k in range(len(listaNomes)):
    if listaNomes[k].lower() in nomeExcepcao:
        listaNomes[k] = listaNomes[k].lower()

nome = " ".join(listaNomes)

print (nome)