class Cromossomo:
    def __init__(self,valor_binario):
        self.valor_binario = valor_binario
        self.apitidao = None
        self.decodificado = None

    def get_apitidao(self):
        return self.apitidao