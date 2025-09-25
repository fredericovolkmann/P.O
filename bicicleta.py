class Bicicleta:
    def __init__(self):
        self.velocidade = 0
        self.andando = False

    def acelerar(self, delta):
        if delta > 0:
            self.velocidade += delta
            self.andando = True

    def frear(self, delta):
        if delta > 0:
            self.velocidade -= delta
            if self.velocidade <= 0:
                self.velocidade = 0
                self.andando = False

    def mostrar_velocidade(self):
        estado = "andando" if self.andando else "parado"
        print(f"Velocidade: {self.velocidade} km/h — Estado: {estado}")


if __name__ == "__main__":
    bike = Bicicleta()
    print("=== Simulador de Bicicleta ===")

    while True:
        print("\nEscolha uma opção:")
        print("1 - Acelerar")
        print("2 - Frear")
        print("3 - Mostrar velocidade")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            delta = int(input("Aumentar em quantos km/h? "))
            bike.acelerar(delta)
        elif opcao == "2":
            delta = int(input("Reduzir em quantos km/h? "))
            bike.frear(delta)
        elif opcao == "3":
            bike.mostrar_velocidade()
        elif opcao == "0":
            print("encerando o simulador. . .")
            break
        else:
            print("opção invalida,tenet novamente.")