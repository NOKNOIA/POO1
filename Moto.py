from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cilindradas):
        super().__init__(marca, modelo, placa,ano)
        self.__cilindradas = cilindradas
    #Sobrescrita do método __str__()
    def __str__(self):
        #Invoco o método __str__() da SUPERCLASSE (Veiculo)
        # Armazeno o retorno na variável "retorno"
        retorno = super().__str__()
        #Retorno a concatenação do valor da variável
        # "retorno" com as "__cilindradas"
        return f'''{retorno}
 - Cilindradas: {self.__cilindradas}'''