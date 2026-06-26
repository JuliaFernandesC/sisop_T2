# Leitura do arquivo
# Vai ler o arquivo txt e tirar os dados que vem com ele:
# - qual o processo + quanto ocupa de memoria -> vira um dicionario

def ler_arquivo(caminh_arq):

    operacoes = []

    with open(caminh_arq, 'r', encoding='utf-8') as arquivo: # encoding='utf-8' evita problemas com acento
        for numero_linha, linha in enumerate(arquivo, start=1): # enumerate para saber qual linha deu erro
            linha = linha.strip()

            if not linha or linha.startswith('#'):
                continue

            linha_upper = linha.upper() #para tratar versoes maiusculas e minusculas -> deixar tudo maiusculo

            if linha_upper.startswith("IN("):
                conteudo = linha[3:-1] # pegar o que esta dentro dos () -> pula os 3 primeiros e o ultimo
                partes   = conteudo.split(",") # pega e coloca numa lista com as duas partes

                if len(partes) != 2:
                    raise ValueError(f"Linha {numero_linha}: formato inválido → '{linha}'")

                processo = partes[0].strip().upper() # diz qual o processo
                tamanho  = int(partes[1].strip()) # converte para inteiro

                if tamanho <= 0:
                    raise ValueError(f"Linha {numero_linha}: tamanho deve ser maior que zero → '{linha}'")

                operacoes.append({ #criar o dicionario
                    "tipo":     "IN",
                    "processo": processo,
                    "tamanho":  tamanho
                })

            elif linha_upper.startswith("OUT("):
                processo = linha[4:-1].strip().upper() # pega so o nome do processo

                if not processo:
                    raise ValueError(f"Linha {numero_linha}: processo não informado → '{linha}'")

                operacoes.append({
                    "tipo":     "OUT",
                    "processo": processo,
                })

            else:
                raise ValueError(f"Linha {numero_linha}: formato inválido → '{linha}'")
            
    return operacoes

# Se precisarmos ver as operacoes no terminal:
# def resumir(operacoes):
#     print(f"Total de operações lidas: {len(operacoes)}\n")
#     for i, op in enumerate(operacoes, start=1):
#         if op["tipo"] == "IN":
#             print(f"  {i:02}. IN  | processo={op['processo']} | tamanho={op['tamanho']}")
#         else:
#             print(f"  {i:02}. OUT | processo={op['processo']}")
