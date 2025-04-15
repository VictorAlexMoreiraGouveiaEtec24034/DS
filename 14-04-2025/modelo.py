# POO (Programação Orientação a objeto)
# Polimorfismo e Herança

# CLasse pai
class Pessoa:
    # Construtor
    def __init__(self, Nome_Complto, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade):
        self.Nome_Completo = Nome_Complto
        self.DiaNascimento = DiaNascimento
        self.MesNascimento = MesNascimento
        self.AnoNascimento = AnoNascimento
        self.Pais = Pais
        self.Cidade = Cidade
        
        self.Trabalha = False
        self.Cargo = None
        self.Empresa = None
        

# Classe filho sendo o Pai a classe 'Pessoa'
class ArvoreGenealogica(Pessoa):
    
    def __init__(self, Nome_Complto, DiaNascimento, MesNascimento, AnoNascimento, PaisOrigem, Cidade, NomeCompleto_Pai, NomeCompleto_Mae):
        super().__init__(Nome_Complto, DiaNascimento, MesNascimento, AnoNascimento, PaisOrigem, Cidade)
        
        self.NomeCompleto_Pai = NomeCompleto_Pai
        self.NomeCompleto_Mae = NomeCompleto_Mae
        
    def Dados_Pessoais(self):
        print(f"Nome-completo: {self.Nome_Completo}")
        print(f"Data-Nascimento: {self.DiaNascimento}/{self.MesNascimento}/{self.AnoNascimento}")
        print(f"País de orgem: {self.Pais}")
        print(f"Cidade Atual: {self.Cidade}")
        print(f"Nome do pai: {self.NomeCompleto_Pai}")
        print(f"Nome do mãe: {self.NomeCompleto_Mae}")
            
            
# # Classe filho sendo o Pai a classe 'Pessoa'
class Profissao(Pessoa):
    def __init__(self, Nome_Complto, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade, Cargo, Empresa):
        super().__init__(Nome_Complto, DiaNascimento, MesNascimento, AnoNascimento, Pais, Cidade)
        
        self.Cargo = Cargo
        self.Empresa = Empresa
        
    def Dados_Colaborador(self):
        print(f"Nome-completo: {self.Nome_Completo}")
        print(f"Data-Nascimento: {self.DiaNascimento}/{self.MesNascimento}/{self.AnoNascimento}")
        print(f"País de origem: {self.Pais}")
        print(f"Cidade Atual: {self.Cidade}")
        print(f"Trabalha: {self.Trabalha}")
        print(f"Cargo: {self.Cargo}")
        print(f"Empresa: {self.Empresa}")