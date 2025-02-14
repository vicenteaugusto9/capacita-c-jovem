def ler_nomes(nome_arquivo):
    """
    Lê os nomes de um arquivo e retorna uma lista.
    """
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        nomes = arquivo.read().splitlines()  # Lê todas as linhas e remove o '\n'
    return nomes