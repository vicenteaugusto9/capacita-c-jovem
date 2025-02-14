# #questão 1 
nome = input("Digite seu nome: ")
print("*Capacita Brasil - Ciclo 2")
print("*Disciplina: Lógica de programação")
print("*Professora: Patrícia Vieira")
print(f"aluno(a):{nome}")

#QUESTÃO 2/3 ACHO QUE ESTA REPETIDA 

#FUNÇÃO DE SOMA COM DADOS DO USUÁRIO
def soma():
    nota1 = float(input("Digite Sua Primeira Nota: "))
    nota2 = float(input("Digite Sua Segunda  Nota: "))
    nota3 = float(input("Digite Sua Terceira  Nota: "))
    nota4= float(input("Digite Sua Quarta Nota: "))
    nota5 = float(input("Digite Sua Quinta  Nota: "))

    # RESULTADO DA SOMA DAS 5 NOTAS DIVIDIDO POR 5 E RESULTADO É A MÉDIA 

    media  = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

    #RETORNO COM RESULTADO
    return media

resultado_media = soma()
print(f"A Média é : {resultado_media}")


#QUESTÃO 4 RECEBENDO OS DADOS DO USER 

salario = float(input("Seu salario:  "))

def valor_do_desconto(salario):

    desconto = salario * 0.11 
    if desconto > 318.20 :
     desconto = 318.20
    return desconto
desconto = valor_do_desconto(salario)

salario_com_desconto = salario - desconto

print(f"O desconto aplicado será: R$ {desconto:.2f}")
print(f"O novo salário após o desconto será: R$ {salario_com_desconto:.2f}")

#QUESTÃO 5 WHILE  

inicio_da_contagem = int(input("Entre Com O Número Inicial Da Contagem: "))
fim_da_contagem = int(input("Entre Com O Número Final Da Contagem: "))

#USANDO WHILE

if inicio_da_contagem >= fim_da_contagem:
    print("Error: O Valor inicial deve ser menor que o final.")
else:
    while inicio_da_contagem <= fim_da_contagem:
        print(inicio_da_contagem)
        inicio_da_contagem += 1


# #QUESTÃO 6

lado1 = int(input("Valor do primeiro lado: "))
lado2 = int(input("Valor do segundo  lado: "))
lado3 = int(input("Valor do terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Formam um Triangulo")
    if lado1 == lado2 == lado3: 
        print("equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 ==lado3 :
        print("isoseles")
    else:
        print("escaleno")

else:
    print("os valores não formam um trianguloo")