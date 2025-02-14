from arquivo import ler_nomes
from lista import filtrar_os_nomes, encontra_maior_nome
from imprimir import imprimir_maior_nome

def main():
    nome_arquivo = 'projeto/nomes.txt'

    nomes = ler_nomes(nome_arquivo)

    nomes_com_a = filtrar_os_nomes(nomes)

    maior_nome = encontra_maior_nome(nomes_com_a)

    imprimir_maior_nome(maior_nome)

if __name__ == "__main__":
    main()