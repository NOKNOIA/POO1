from Veiculo import Veiculo
class Caminhao (Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    #Override - Sobrescrever o méto __str__()
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
    - Capacidade: {self.__capacidade}''' 