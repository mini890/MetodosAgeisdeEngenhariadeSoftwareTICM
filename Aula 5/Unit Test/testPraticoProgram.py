def corrigirNome(s):
    # s = "1"
    listaNomes = s.title().split()
    nomeExcepcao = ["de", "da", "das", "do", "dos", "e"]

    for k in range(len(listaNomes)):
        if listaNomes[k].lower() in nomeExcepcao:
            listaNomes[k] = listaNomes[k].lower()

    return " ".join(listaNomes)
