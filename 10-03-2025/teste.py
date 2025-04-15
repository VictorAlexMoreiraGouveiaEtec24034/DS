try:
    dado = "palavra"
    dado2 = int(dado) + 10
    
except ValueError as Error:
    print(Error)
    print("Não foi possivel converter para int por ser um string")
