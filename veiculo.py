class Veiculo:
    def __init__(self, capacidade_reservatorio, km_por_litro):
        self.capacidade_reservatorio = capacidade_reservatorio
        self.km_por_litro = km_por_litro
        self.combustivel_atual = capacidade_reservatorio
        self.distancia_total_percorrida = 0.0

    def andar(self, distancia):
        if distancia <= 0:
            print("A distância a ser percorrida deve ser positiva.")
            return

        combustivel_necessario = distancia / self.km_por_litro

        if combustivel_necessario <= self.combustivel_atual:
            self.combustivel_atual -= combustivel_necessario
            self.distancia_total_percorrida += distancia
            print(f"O veículo percorreu {distancia:.2f} KM.")
            print(f"Combustível restante: {self.combustivel_atual:.2f} L.")
        else:
            distancia_maxima = self.combustivel_atual * self.km_por_litro
            self.distancia_total_percorrida += distancia_maxima
            self.combustivel_atual = 0.0
            print(f"Combustível insuficiente para percorrer {distancia:.2f} KM.")
            print(f"O veículo percorreu apenas {distancia_maxima:.2f} KM e parou por falta de combustível.")

    def mostrarAutonomia(self):
        autonomia = self.combustivel_atual * self.km_por_litro
        print(f"Autonomia restante: O veículo pode percorrer mais {autonomia:.2f} KM.")
        return autonomia

    def mostrarDistanciaPercorrida(self):
        print(f"Distância total percorrida: {self.distancia_total_percorrida:.2f} KM.")
        return self.distancia_total_percorrida
    
    def abastecer(self, litros):
        if litros <= 0:
            print("A quantidade de litros para abastecer deve ser positiva.")
            return

        espaco_livre = self.capacidade_reservatorio - self.combustivel_atual
        litros_abastecidos = min(litros, espaco_livre)

        self.combustivel_atual += litros_abastecidos
        print(f"Abastecidos {litros_abastecidos:.2f} L. Tanque agora com {self.combustivel_atual:.2f} L.")
        
        if litros > espaco_livre:
            print(f"Atenção: {litros - espaco_livre:.2f} L transbordaram, pois o tanque estava cheio.")


class Carro(Veiculo):
    def __init__(self, capacidade_reservatorio, km_por_litro, numero_portas):
        super().__init__(capacidade_reservatorio, km_por_litro)
        self.numero_portas = numero_portas
        print(f"\nCarro criado: {numero_portas} portas, Tanque {capacidade_reservatorio}L, Rendimento {km_por_litro} KM/L.")

    def ligar_radio(self):
        print("Rádio ligado! Toca uma música para a viagem.")


class Moto(Veiculo):
    def __init__(self, capacidade_reservatorio, km_por_litro, cilindradas):
        super().__init__(capacidade_reservatorio, km_por_litro)
        self.cilindradas = cilindradas
        print(f"\nMoto criada: {cilindradas}cc, Tanque {capacidade_reservatorio}L, Rendimento {km_por_litro} KM/L.")

    def empinar(self):
        print("Atenção! Manobra perigosa: A moto empinou!")

def criar_carro_usuario():
    print("\n--- CRIAÇÃO DE CARRO ---")
    try:
        capacidade = float(input("Capacidade do reservatório (Litros): "))
        rendimento = float(input("Rendimento (KM por Litro): "))
        portas = int(input("Número de portas: "))
        return Carro(capacidade, rendimento, portas)
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
        return None

def criar_moto_usuario():
    print("\n--- CRIAÇÃO DE MOTO ---")
    try:
        capacidade = float(input("Capacidade do reservatório (Litros): "))
        rendimento = float(input("Rendimento (KM por Litro): "))
        cilindradas = int(input("Cilindradas (cc): "))
        return Moto(capacidade, rendimento, cilindradas)
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
        return None

# Criando e testando o Carro
meu_carro = criar_carro_usuario()
if meu_carro:
    print("\n--- AÇÕES DO CARRO ---")
    meu_carro.ligar_radio()
    
    try:
        distancia_carro = float(input("Quantos KM o carro deve andar? "))
        meu_carro.andar(distancia_carro)
        meu_carro.mostrarAutonomia()
        
        litros_abastecer_carro = float(input("Quantos litros deseja abastecer? "))
        meu_carro.abastecer(litros_abastecer_carro)
        meu_carro.mostrarDistanciaPercorrida()
    except ValueError:
        print("Erro: Por favor, insira um número para distância/abastecimento.")


# Criando e testando a Moto
minha_moto = criar_moto_usuario()
if minha_moto:
    print("\n--- AÇÕES DA MOTO ---")
    minha_moto.empinar()
    
    try:
        distancia_moto = float(input("Quantos KM a moto deve andar? "))
        minha_moto.andar(distancia_moto)
        minha_moto.mostrarAutonomia()
        minha_moto.mostrarDistanciaPercorrida()
    except ValueError:
        print("Erro: Por favor, insira um número para distância.")