class Contador:
    
    def __init__(self, valor_inicial=0):
      
        if valor_inicial < 0:
            self._valor_atual = 0
            print("O valor inicial não pode ser negativo. Contador iniciado em 0.")
        else:
            self._valor_atual = valor_inicial
            print(f"Contador criado, iniciado em: {self._valor_atual}")

    
    def zerar(self):
        """
        Zera a contagem atual.
        """
        self._valor_atual = 0
        print("Contagem zerada.")


    def incrementar(self, quantidade=1):
     
        if isinstance(quantidade, int) and quantidade > 0:
            self._valor_atual += quantidade
        elif quantidade <= 0:
            print("A quantidade de incremento deve ser um inteiro positivo.")
        else:
            print("Parâmetro inválido. Use um número inteiro positivo.")


    def decrementar(self, quantidade=1):
     
        if isinstance(quantidade, int) and quantidade > 0:
            if self._valor_atual >= quantidade:
                self._valor_atual -= quantidade
            else:
               
                self._valor_atual = 0
                print("Decremento excedeu o valor. Contagem definida para 0.")
        elif quantidade <= 0:
            print("A quantidade de decremento deve ser um inteiro positivo.")
        else:
            print("Parâmetro inválido. Use um número inteiro positivo.")
            
   
    
    def get_valor_atual(self):
       
        return self._valor_atual


print("--- Testando Construtores ---")

c1 = Contador() 

c2 = Contador(valor_inicial=10) 

print(f"\nC1 inicial: {c1.get_valor_atual()}")
print(f"C2 inicial: {c2.get_valor_atual()}")

print("\n--- Testando Sobrecarga do Incrementar ---")

c1.incrementar() 
print(f"C1 após incremento (padrão): {c1.get_valor_atual()}") # 1

c2.incrementar(5) 
print(f"C2 após incremento (por valor): {c2.get_valor_atual()}") # 15

print("\n--- Testando Sobrecarga do Decrementar ---")

c2.decrementar() 
print(f"C2 após decremento (padrão): {c2.get_valor_atual()}") # 14


c2.decrementar(7) 
print(f"C2 após decremento (por valor): {c2.get_valor_atual()}") # 7

print("\n--- Testando Zerar ---")
c2.zerar()
print(f"C2 após zerar: {c2.get_valor_atual()}") # 0