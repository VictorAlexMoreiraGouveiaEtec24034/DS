import random

class Banco:
    def __init__(self):
        self.QtdPessoa = 0
        self.User = []
        self.Password = []
        self.SaldoPessoas = []
        
    def Cadastrar(self):
        print("Preencha os dados para se cadastrar")
        User = input("Nome-Completo: ")
        Passwd = input("Senha: ")
        
        # Adicionando dados a banco
        self.User.append(User)
        self.Password.append(Passwd)
        self.QtdPessoa = self.QtdPessoa + 1
    
    def Login(self):
        print("Preenchar os dados para entrar na conta")
        User = input("Nome: ")
        Passwd = input("Senha: ")
        
        # Validação dos dados
        try:
            IndiceUser = self.User.index(User)
            IndicePassword = self.Password.index(Passwd)
        
        except ValueError as Error:
            print("Não foi possivel localizar os dados")
            
               
        else:
            if ((self.User[IndiceUser] == User) and (self.Password[IndicePassword] == Passwd)):
                print("Autenticação correta")
                return self.User[IndiceUser]
            
            else:
                print("Dados incorretos")
                
                
    # Fazer sistema de transferencia de saldo bancario usando a lib random para gerar a chave de transferencia