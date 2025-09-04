import os

# Define o caminho do arquivo para ser salvo
CAMINHO_DO_ARQUIVO = r"C:\Users\frederico lindo\Downloads\lab\lab_equipamentos.txt"

# --- Classe Base ---
class Equipamento:
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str):
        self.id_equipamento = id_equipamento
        self.cor = cor
        self.tamanho = tamanho
        self.formato = formato

    def __str__(self):
        return f"ID: {self.id_equipamento}, Cor: {self.cor}, Tamanho: {self.tamanho}, Formato: {self.formato}"

# --- Classes Derivadas (Herança) ---
class ComponenteEletronico(Equipamento): # Herda de Equipamento
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, marca: str, modelo: str):
        super().__init__(id_equipamento, cor, tamanho, formato)
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{super().__str__()} | Marca: {self.marca}, Modelo: {self.modelo}"

class CPU(ComponenteEletronico): # Herda de ComponenteEletronico
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, marca: str, modelo: str, processador: str):
        super().__init__(id_equipamento, cor, tamanho, formato, marca, modelo)
        self.processador = processador

    def __str__(self):
        return f"{super().__str__()} | Processador: {self.processador}"

class Monitor(ComponenteEletronico): # Herda de ComponenteEletronico
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, marca: str, modelo: str, resolucao: str):
        super().__init__(id_equipamento, cor, tamanho, formato, marca, modelo)
        self.resolucao = resolucao

    def __str__(self):
        return f"{super().__str__()} | Resolução: {self.resolucao}"

class Mobiliario(Equipamento): # Herda de Equipamento
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, material: str):
        super().__init__(id_equipamento, cor, tamanho, formato)
        self.material = material

    def __str__(self):
        return f"{super().__str__()} | Material: {self.material}"

class Mesa(Mobiliario): # Herda de Mobiliario
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, material: str, superficie: str):
        super().__init__(id_equipamento, cor, tamanho, formato, material)
        self.superficie = superficie

    def __str__(self):
        return f"{super().__str__()} | Superfície: {self.superficie}"

class Cadeira(Mobiliario): # Herda de Mobiliario
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, material: str, ajuste_altura: bool):
        super().__init__(id_equipamento, cor, tamanho, formato, material)
        self.ajuste_altura = ajuste_altura

    def __str__(self):
        return f"{super().__str__()} | Ajuste de Altura: {'Sim' if self.ajuste_altura else 'Não'}"

class CadeiraGiratoria(Cadeira): # Herda de Cadeira
    def __init__(self, id_equipamento: str, cor: str, tamanho: str, formato: str, material: str, ajuste_altura: bool, rodinhas: bool):
        super().__init__(id_equipamento, cor, tamanho, formato, material, ajuste_altura)
        self.rodinhas = rodinhas

    def __str__(self):
        return f"{super().__str__()} | Possui Rodinhas: {'Sim' if self.rodinhas else 'Não'}"

# --- Classe de Associação ---
class Laboratorio:
    def __init__(self, nome: str):
        self.nome = nome
        self.equipamentos = []

    def adicionar_equipamento(self, equipamento: Equipamento):
        self.equipamentos.append(equipamento)
        print(f"✅ {equipamento.__class__.__name__} '{equipamento.id_equipamento}' adicionado ao laboratório '{self.nome}'.")

    def listar_equipamentos(self):
        if not self.equipamentos:
            print("Nenhum equipamento cadastrado na lista atual.")
        else:
            print(f"\n--- Equipamentos do Laboratório: {self.nome} ---")
            for eq in self.equipamentos:
                print(eq)
                print() 

    def salvar_para_arquivo(self, caminho_arquivo: str):
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(f"--- Equipamentos do Laboratório: {self.nome} ---\n\n")
                if not self.equipamentos:
                    f.write("Nenhum equipamento cadastrado.")
                else:
                    for eq in self.equipamentos:
                        f.write(str(eq) + "\n\n")
            print(f" Lista de equipamentos salva com sucesso em '{caminho_arquivo}'")
        except Exception as e:
            print(f" Erro ao salvar o arquivo: {e}")

    def remover_equipamento(self, id_equipamento: str):
        item_removido = None
        for eq in self.equipamentos:
            if eq.id_equipamento == id_equipamento:
                item_removido = eq
                break
        
        if item_removido:
            self.equipamentos.remove(item_removido)
            print(f" Equipamento com ID '{id_equipamento}' removido com sucesso.")
        else:
            print(f" Erro: Nenhum equipamento encontrado com o ID '{id_equipamento}'.")


def visualizar_arquivo(caminho_arquivo: str):
    """Lê e exibe o conteúdo de um arquivo de texto."""
    if not os.path.exists(caminho_arquivo):
        print(f" O arquivo '{caminho_arquivo}' não existe.")
        return

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            print(f"\n--- Conteúdo do Arquivo: {caminho_arquivo} ---")
            print(conteudo)
            print("-------------------------------------------\n")
    except Exception as e:
        print(f" Erro ao ler o arquivo: {e}")


def menu():
    """Função principal que gerencia o menu e a interação do usuário."""
    lab_informatica = Laboratorio("Laboratório de Programação 1")
    
    
    lab_informatica.adicionar_equipamento(CPU("CPU 2019012336", "preto", "Pequeno", "Cúbico", "Intel", "Core i7", "i7-10700K"))
    lab_informatica.adicionar_equipamento(Monitor("MON 20199012913", "preto", "Médio", "Retangular", "Daten", " 22mp55pj-b", "1920x1080"))
    lab_informatica.adicionar_equipamento(Mesa("MESA2021002821", "bege", "Grande", "Retangular", "Madeira", "Lisa"))
    lab_informatica.adicionar_equipamento(CadeiraGiratoria("CG2022002128", "azul", "Médio", "Ergonômica", "Plástico/Metal", True, True))

    while True:
        print("\n=== Menu de Gerenciamento do Laboratório ===")
        print("1. Adicionar novo equipamento")
        print("2. Remover equipamento por ID")
        print("3. Listar equipamentos em memória (na tela)")
        print("4. Salvar lista de equipamentos no arquivo")
        print("5. Visualizar o conteúdo do arquivo")
        print("6. Sair")

        escolha = input("Digite sua opção: ")

        if escolha == '1':
            tipo = input("Digite o tipo de equipamento (CPU, Monitor, Mesa, Cadeira, CadeiraGiratoria): ").capitalize()
            id_eq = input("ID do equipamento: ")
            cor_eq = input("Cor: ")
            tamanho_eq = input("Tamanho: ")
            formato_eq = input("Formato: ")
            
            if tipo == 'Cpu':
                marca_eq = input("Marca: ")
                modelo_eq = input("Modelo: ")
                processador_eq = input("Processador: ")
                novo_eq = CPU(id_eq, cor_eq, tamanho_eq, formato_eq, marca_eq, modelo_eq, processador_eq)
                lab_informatica.adicionar_equipamento(novo_eq)
            elif tipo == 'Monitor':
                marca_eq = input("Marca: ")
                modelo_eq = input("Modelo: ")
                resolucao_eq = input("Resolução: ")
                novo_eq = Monitor(id_eq, cor_eq, tamanho_eq, formato_eq, marca_eq, modelo_eq, resolucao_eq)
                lab_informatica.adicionar_equipamento(novo_eq)
            elif tipo == 'Mesa':
                material_eq = input("Material: ")
                superficie_eq = input("Superfície: ")
                novo_eq = Mesa(id_eq, cor_eq, tamanho_eq, formato_eq, material_eq, superficie_eq)
                lab_informatica.adicionar_equipamento(novo_eq)
            elif tipo == 'Cadeira':
                material_eq = input("Material: ")
                ajuste_altura_eq = input("Possui ajuste de altura? (sim/não): ").lower() == 'sim'
                novo_eq = Cadeira(id_eq, cor_eq, tamanho_eq, formato_eq, material_eq, ajuste_altura_eq)
                lab_informatica.adicionar_equipamento(novo_eq)
            elif tipo == 'Cadeiragiratoria':
                material_eq = input("Material: ")
                ajuste_altura_eq = input("Possui ajuste de altura? (sim/não): ").lower() == 'sim'
                rodinhas_eq = input("Possui rodinhas? (sim/não): ").lower() == 'sim'
                novo_eq = CadeiraGiratoria(id_eq, cor_eq, tamanho_eq, formato_eq, material_eq, ajuste_altura_eq, rodinhas_eq)
                lab_informatica.adicionar_equipamento(novo_eq)
            else:
                print(" Tipo de equipamento inválido.")

        elif escolha == '2':
            if not lab_informatica.equipamentos:
                print("A lista está vazia, não há o que remover.")
                continue
            
            print("\nEquipamentos atuais:")
            for eq in lab_informatica.equipamentos:
                print(f"ID: {eq.id_equipamento} | Tipo: {eq.__class__.__name__}")
            
            id_remover = input("\nDigite o ID do equipamento a ser removido: ")
            lab_informatica.remover_equipamento(id_remover)

        elif escolha == '3':
            lab_informatica.listar_equipamentos()
        
        elif escolha == '4':
            lab_informatica.salvar_para_arquivo(CAMINHO_DO_ARQUIVO)
        
        elif escolha == '5':
            visualizar_arquivo(CAMINHO_DO_ARQUIVO)
        
        elif escolha == '6':
            print("Saindo do programa.")
            break
        
        else:
            print(" Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()