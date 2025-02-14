def filtrar_os_nomes(nomes):
    """
    Filtra os nomes que começam com 'A' ou 'a'.
    """
    return [nome for nome in nomes if nome.lower().startswith('a')]

def encontra_maior_nome(nomes):
    """
    Retorna o maior nome da lista.
    """
    return max(nomes, key=len) if nomes else None