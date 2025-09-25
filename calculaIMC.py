class Pessoa:
    
    def __init__(self, nome, altura_cm, peso):
        self.nome = nome
        self.peso = peso
        self.altura_m = altura_cm /100
        
    def calcular_IMC(self):
       
        IMC = self.peso / (self.altura_m**2)
        return IMC
    
nome = input("escreva o  seu nome: ")
peso = float(input("qual o seu peso: "))
altura_cm = float(input("qual a sua altura: "))

a1 = Pessoa(nome,altura_cm,peso)
print(f"{a1.nome} tem IMC: {a1.calcular_IMC(): .2f}")