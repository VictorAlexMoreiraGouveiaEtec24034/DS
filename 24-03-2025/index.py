# Classe base do carro
class Carro:
    def __init__(self, Marca, Modelo, Ano):
        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.Velcidade = 0
        
    def Acelerar(self, Valor):
        print(f"Carro acelerando há {Valor}Km/h")
        self.Velcidade = Valor
        
    def Freiar(self, Valor):
        print("Diminuindo a velocidade")
        
    def mostrar_info(self):
        print(f"Marca: {self.Marca}")
        print(f"Modelo: {self.Modelo}")
        print(f"Ano: {self.Modelo}")
        
    def buzinar(self):
        print("Biiip! Biiip!")
    
# Instancias
Carro1 = Carro("Toyota", "Corolla", 2022)
Carro1.Acelerar(50)
Carro1.Freiar(20)
Carro1.mostrar_info()