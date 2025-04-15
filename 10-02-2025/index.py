import sys
from Configs_Colors import *

# Mini Banco Dados
nomes = []
dias_nascimentos = []
meses_nascimento = []
anos_nascimentos = []
ciadades_nascimentos = []
paises_nascimento = []

class Pessoa:    
    def cadastrar(self, nome, dia, mes, ano, cidade, pais):
        nomes.append(nome)

        dias_nascimentos.append(dia)
        meses_nascimento.append(mes)
        anos_nascimentos.append(ano)
        ciadades_nascimentos.append(cidade)
        paises_nascimento.append(pais)
        

    def exibir_dados(self, nome, dia, mes, ano, cidade, pais):
        print()
        print(f"{FONT_AMARELO}Nome-completo:{END}{FONT_CIANO} {nome}{END}")
        print(f"{FONT_AMARELO}Data-Nascimento:{END} {FONT_CIANO}{dia_nascimento}/0{mes_nascimento}/{ano_nascimento}{END}")
        print(f"{FONT_AMARELO}País de origem:{END} {FONT_CIANO}{pais_nascimento}{END}")
        print(f"{FONT_AMARELO}Cidade-Nascimento:{END} {FONT_CIANO}{cidade_nascimento}{END}")


if __name__ == "__main__":
    nome_completo = input("Qual é o seu nome?: ")
    dia_nascimento = int(input("Qual é o seu dia de nascimento?: "))
    mes_nascimento = int(input("Qual é o seu mês de nascimento?: "))
    ano_nascimento = int(input("Qual é o seu ano de nascimento?: "))
    cidade_nascimento = input("Qual cidade você nasceu?: ")
    pais_nascimento = input("Qual país você nasceu?: ")

    pessoa1 = Pessoa()
    pessoa1.cadastrar(nome_completo, dia_nascimento, mes_nascimento, ano_nascimento, cidade_nascimento, pais_nascimento)

    i = 0
    while len(nomes) > i:
        pessoa1.exibir_dados(nomes[i], dias_nascimentos[i], meses_nascimento[i], anos_nascimentos[i], ciadades_nascimentos[i], paises_nascimento[i])
        i = i + 1
    sys.exit()
