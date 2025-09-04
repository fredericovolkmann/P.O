class Mesa():
    def __init__ (self,altura, formato,cor):
        self.altura = altura
        self.formato = formato
        self.cor = cor
    def __str__ (self):
        return f"mesa tem {self.altura} altura, {self.formato} de formato, e {self.cor}, de cor"
    def apoiar(self,objeto):
        return f"segurando o {objeto}"
class Computador():
    def __init__(self, monitor,cpu, perifericos):
        self.monitor = monitor
        self.cpu = cpu
        self.perifericos = perifericos
    def ligar(self):
        print("o computador está ligando")
    def desligar(self):
        print("desligando...")
    def escrever(self,perifericos):
        x = input("digite algo que o pc vai escrever")
        print(x)
class Parede():
    def __init__(self,altura,cor,comprimento):
        self.altura = altura
        self.cor = cor
        self.comprimento = comprimento
    def segurar(self):
        return f"sirvo pra segurar"
    
class Ar_condicionado(Parede):
    def __init__(self, formato,BTU,cor):
        self.formato = formato
        self.BTU = BTU
        self.cor = cor
    def gelar(self):
        return f"estou gelando"
    def segurar(self):
        return super().segurar() + " E a parede está me segurando"
class Cadeira_giratoria():
    def __init__(self, rodas,cor, alavanca,altura):
        self.rodas = rodas
        self.cor = cor
        self.alavanca = alavanca
        self.altura = altura
    def aumentar_altura(self,altura):
        self.altura = altura
    def diminuir_altura(self,altura):
        self.altura = -altura
    def sentar(self):
        return f"estou sentando na cadeira"
class Tomada(Parede):
    def __init__(self,tamanho, furos,cor, formato):
        self.tamanho = tamanho
        self.furos = furos
        self.cor = cor
        self.formato = formato
    def fornecer_energia(self,plug):
        if plug == True:
            print("estou conectado e fornecendo energia")
        else: 
            print("Não estou conectado")
    def segurar(self):
        return super().segurar() + " e a tomada fica na parede"