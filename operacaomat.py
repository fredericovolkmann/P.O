from abc import ABC, abstractmethod

# --- Classes de Operação Matemática ---

class OperacaoMatematica(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    @abstractmethod
    def calcular(self):
        pass

class Soma(OperacaoMatematica):
    def calcular(self):
        return self.a + self.b

class Subtracao(OperacaoMatematica):
    def calcular(self):
        return self.a - self.b

class Multiplicacao(OperacaoMatematica):
    def calcular(self):
        return self.a * self.b

class Divisao(OperacaoMatematica):
    def calcular(self):
        if self.b == 0:
            return "Erro: Divisão por zero não é permitida."
        return self.a / self.b

# --- Função Principal para Interação com o Usuário ---

def calculadora_interativa():
    print("--- Calculadora Interativa (POO) ---")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return

    print("\nEscolha a operação:")
    print("1: Soma (+)")
    print("2: Subtração (-)")
    print("3: Multiplicação (*)")
    print("4: Divisão (/)")
    
    escolha = input("Digite o número da operação (1/2/3/4): ")

    operacao = None
    simbolo = ""
    
    if escolha == '1':
        operacao = Soma(num1, num2)
        simbolo = "+"
    elif escolha == '2':
        operacao = Subtracao(num1, num2)
        simbolo = "-"
    elif escolha == '3':
        operacao = Multiplicacao(num1, num2)
        simbolo = "*"
    elif escolha == '4':
        operacao = Divisao(num1, num2)
        simbolo = "/"
    else:
        print("Escolha de operação inválida.")
        return

    resultado = operacao.calcular()

    print("\n--- Resultado ---")
    print(f"Operação: {num1} {simbolo} {num2}")
    print(f"Resultado: {resultado}")
    print("-----------------\n")

if __name__ == "__main__":
    calculadora_interativa()