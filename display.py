# Vai ficar responsavel de mostrar como esta a memoria
# a cada operacao de IN e OUT. 

def exibir_memoria(blocos, total=False): #opcao de mostrar a mem todal ou nao
    
    if total:
        print("  Memória: ", end="")
        for bloco in blocos:
            if bloco["processo"] is None:
                print(f"| {bloco['tamanho']} |", end=" ")
            else:
                print(f"| {bloco['processo']}({bloco['tamanho']}) |", end=" ")
        print()
    else:
        print("  Blocos livres: ", end="")
        tem_livre = False

        for bloco in blocos:
            if bloco["processo"] is None:
                print(f"| {bloco['tamanho']} |", end=" ")
                tem_livre = True

        if not tem_livre:
            print("nenhum")
        else:
            print()


def fragmentacao_total(blocos):
    
    total = 0
    for bloco in blocos:
        if bloco["processo"] is not None:
            total += bloco.get("fragmentacao", 0)

    print(f"  Fragmentação interna total: {total}")

def fragmentacao_bloco(processo, tamanho_pedido, tamanho_bloco):
    
    fragmentacao = tamanho_bloco - tamanho_pedido
    if fragmentacao > 0:
        print(f"  Fragmentação interna: processo {processo} ocupou {tamanho_bloco} de {tamanho_pedido}, fragmentação = {fragmentacao}")



def operacao_atual(operacao):
    
    if operacao["tipo"] == "IN":
        print(f"\n>> IN({operacao['processo']}, {operacao['tamanho']})")
    else:
        print(f"\n>> OUT({operacao['processo']})")
