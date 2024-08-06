from classe import*
from function import*
def menu_principal():
    print("1-Criar cao: ")
    print("2-Criar pessoa: ")
    print("3-Listar cão: ")
    print("4-Listar pessoa: ")
    print("5-Excluir cachorro: ")
    print("6-Excluir humano: ")
    print()

def listar_humano():
    num=1

    for humano in lista_de_humano:
        print(f'{"Nome"}: {humano.nome}\n')
        print(f'{"Cor"}: {humano.cor}\n')
        print(f'{"Peso"}: {humano.peso}\n')
        print(f'{"Tamanho"}: {humano.tamanho}\n')
        
        num+=1
def listar_cao():
    num=1

    for cao in lista_de_cao:
        print(f'{"Nome cachorro"}: {cao.nome}\n')
        print(f'{"Tamanho cachorro"}: {cao.tamanho}\n')
        print(f'{"Raça"}: {cao.raca}\n')
        print(f'{"Racionalidade"}: {cao.racional}\n')

        num+=1
