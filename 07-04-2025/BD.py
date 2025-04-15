"""Sistema de banco de dados"""

# importações de libs e arquivos
from Terminal import *

class BD:
    def __init__(self, nome):
        self.nome = nome
        self.qtd_tabelas = int
        self.nome_tabelas = []
    
    def view_status(self):
        print(f"Nome do banco: {self.nome}")
        print(f"Quantidade de tabela: {self.qtd_tabelas}")
        print(f"Tabelas-existentes: {self.nome_tabelas}")
        
    