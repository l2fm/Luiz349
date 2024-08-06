from classe import*
from view import*
from function import*
def criar_cao():
    nome=input("Digite o nome do cão: ")
    tamanho=input("Tamanho em cm: ")
    raca=input("Raça: ")
    racional=False
    cao=Cachorro(nome,tamanho,raca,racional)
    lista_de_cao.append(cao)
def excluir_cao():
    nome=input("Digite o nome do cachorro: ")
    for ch in lista_de_cao:
        if ch.nome==nome:
            lista_de_cao.remove(ch)

def criar_humano():
    nome=input("Digite o nome: ") 
    tamanho=input("Tamanho em cm: ") 
    cor=input("Digite a cor: ")
    peso=input("Digite o peso: ")
    humano=Humano(nome,cor,peso,tamanho)
    lista_de_humano.append(humano)

def excluir_humano():
    nome=input("Digite o nome do humano: ")
    for ps in lista_de_humano:
        if ps.nome==nome:
            lista_de_cao.remove(ps)

def excluir_humano():
    lista_de_humano.remove()
    print(criar_humano.nome)


while True:
    menu_principal()
    op=int(input("Opção: "))
    if 1==op:
        criar_cao()

    elif 2==op:
        criar_humano()

    elif 3==op:
        listar_cao()
    elif 4==op:
        listar_humano()
    
    elif 5==op:
        excluir_cao()
    elif 6==op:
        excluir_humano()