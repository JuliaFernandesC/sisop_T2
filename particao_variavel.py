# Responsável pela alocação de memória com partições variáveis
# algoritmos de Circular-Fit e Worst-Fit

def criar_memoria(tamanho): # inicialmente com um bloco unico livre
    return [{"tipo": "H", "inicio": 0, "tamanho": tamanho}]

ponteiro = 0  # índice do nó onde a próxima busca começa

def circular_fit_in(blocos, processo, tamanho):
    global ponteiro

    tamanho_lista = len(blocos)
    
    # Percorre a lista a partir do ponteiro, dando uma volta completa
    for i in range(tamanho_lista):
        indice = (ponteiro + i) % tamanho_lista  # volta ao início quando chega no fim

        bloco = blocos[indice]

        if bloco["tipo"] == "H" and bloco["tamanho"] >= tamanho:

            if bloco["tamanho"] == tamanho:
                # Tamanho exato: só muda o tipo
                bloco["tipo"] = "P"
                bloco["processo"] = processo

            else:
                # divide em dois = parte ocupada e parte livre
                sobra = bloco["tamanho"] - tamanho

                bloco["tipo"] = "P"
                bloco["tamanho"] = tamanho
                bloco["processo"] = processo

                novo_hole = {"tipo": "H", "inicio": bloco["inicio"] + tamanho, "tamanho": sobra}
                blocos.insert(indice + 1, novo_hole) #ver se esta inserindo no lugar certo

            # Ponteiro avança para o nó seguinte ao alocado
            ponteiro = (indice + 1) % len(blocos)
            return True  # alocação bem sucedida

    return False  # não encontrou espaço

def circular_fit_out(blocos, processo):
    global ponteiro

    # Acha o índice do processo
    indice = None
    for i, bloco in enumerate(blocos):
        if bloco.get("processo") == processo:
            indice = i
            break

    if indice is None:
        print(f"  Processo {processo} não encontrado na memória.")
        return

    # Libera o bloco
    blocos[indice]["tipo"] = "P"
    del blocos[indice]["processo"]
    blocos[indice]["tipo"] = "H"

    # Tenta juntar com o vizinho à direita
    if indice + 1 < len(blocos) and blocos[indice + 1]["tipo"] == "H":
        blocos[indice]["tamanho"] += blocos[indice + 1]["tamanho"]
        blocos.pop(indice + 1)

    # Tenta juntar com o vizinho à esquerda
    if indice - 1 >= 0 and blocos[indice - 1]["tipo"] == "H":
        blocos[indice - 1]["tamanho"] += blocos[indice]["tamanho"]
        blocos.pop(indice)
        indice = indice - 1  # atualiza o índice para o nó resultante

    # Ponteiro fica no nó resultante da liberação
    ponteiro = indice % len(blocos)