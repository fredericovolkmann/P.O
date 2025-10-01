from abc import ABC, abstractmethod
import math

class Forma(ABC):
    _quantidade_objetos = 0

    def __init__(self):
        Forma._quantidade_objetos += 1

    @abstractmethod
    def calcularArea(self):
        pass
    
    @classmethod
    def mostrarQuantidadeObjetos(cls):
        print(f"Total de objetos 'Forma' (e suas subclasses) criados: {cls._quantidade_objetos}")
        return cls._quantidade_objetos

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio
        
    def calcularArea(self):
        return math.pi * (self.raio ** 2)

class Quadrado(Forma):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado
        
    def calcularArea(self):
        return self.lado * self.lado

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return (self.base * self.altura) / 2

def coletar_dados_e_calcular():
    formas = []
    
    print("--- Calculadora de Áreas de Formas (POO) ---")

    # Círculo
    try:
        raio = float(input("\nDigite o raio do Círculo: "))
        formas.append(Circulo(raio))
    except ValueError:
        print("Entrada inválida para o Círculo. Usando raio padrão (1).")
        formas.append(Circulo(1))

    # Quadrado
    try:
        lado = float(input("Digite o lado do Quadrado: "))
        formas.append(Quadrado(lado))
    except ValueError:
        print("Entrada inválida para o Quadrado. Usando lado padrão (1).")
        formas.append(Quadrado(1))
    
    # Triângulo
    try:
        base = float(input("Digite a base do Triângulo: "))
        altura = float(input("Digite a altura do Triângulo: "))
        formas.append(Triangulo(base, altura))
    except ValueError:
        print("Entrada inválida para o Triângulo. Usando base e altura padrão (1).")
        formas.append(Triangulo(1, 1))

    print("\n--- Resultados ---")
    
    for forma in formas:
        if isinstance(forma, Circulo):
            print(f"Área do Círculo (raio {forma.raio}): {forma.calcularArea():.2f}")
        elif isinstance(forma, Quadrado):
            print(f"Área do Quadrado (lado {forma.lado}): {forma.calcularArea():.2f}")
        elif isinstance(forma, Triangulo):
            print(f"Área do Triângulo (base {forma.base}, altura {forma.altura}): {forma.calcularArea():.2f}")
    
    print("------------------")
    
    Forma.mostrarQuantidadeObjetos()

if __name__ == "__main__":
    coletar_dados_e_calcular()