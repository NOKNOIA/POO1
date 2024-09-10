class Veiculo:
    # __init_ => é o método construtor
    def __init__(self, marca, modelo, placa, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__placa = placa
        self.__ano = ano
    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca
    # Método de instância
    def calcularTempoUso(self):
        return 2024 - self.__ano
    def __str__(self):
        return f'''Marca: {self.__marca}
    - Modelo: {self.__modelo}
    - Placa: {self.__placa}
    - Ano: {self.__ano}'''
        
