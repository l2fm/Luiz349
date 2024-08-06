class Animal:
    nome=str
    coracao:bool
    racional=bool
    tamanho=float
    cor=str
    def __init__(self,nome,tamanho,cor,coracao,racional):
        self.nome=nome
        self.coracao=coracao
        self.racional=racional
        self.tamanho=tamanho
        self.cor=cor

class Humano(Animal):
    def __init__(self, nome,cor,peso,tamanho):
        self.nome=nome
        self.cor=cor
        self.tamanho=tamanho
        self.racional=True
        self.peso=peso
class Cachorro(Animal):
    raca=""
    def __init__(self,nome,tamanho,raca,racional):
        self.nome=nome
        self.tamanho=tamanho
        self.raca=raca
        self.racional=racional

