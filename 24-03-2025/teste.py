import pdb

def Calcular_Idade(age):

    quest1 = input("Você já fez aniversario esse ano?:(S/N) ")
    
    if (quest1 == 's' or quest1 == 'S'):
        calc = 2024 - age + 1 
        print(f"Sua idade é {calc}")
        
    elif(quest1 == 'n' or quest1 == 'N'):
        calc = 2024 - age
        print(f"Sua idade é {calc}")
        
    else:
        print("Dado não permitido")


age = int(input("Qual o seu ano de nascimento?: "))
pdb.set_trace()
Calcular_Idade(age)
