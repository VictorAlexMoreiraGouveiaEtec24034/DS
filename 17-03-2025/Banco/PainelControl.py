from Banco.Bank import Banco

class ControlPainel:
    def __init__(self, UserName):
        self.ControlHome = "(BANK/ )> "
        
        # Dados de usuário
        self.User = UserName
        
    def View(self):
        return input(self.ControlHome)
    
    def Help(self):
        print("")
        print("1) Fazer Login")
        print("2) Cadastrar usuário")
    
# Lógica do Painel de controle do sistema
while True:
    cmd = ControlPainel.View()
    
    match cmd:
        
        case "1":
            NameUser = Banco.Login()
            register = ControlPainel(NameUser)
            
        case "2":
            Banco.Cadastrar()