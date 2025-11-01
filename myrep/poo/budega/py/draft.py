class Pessoa:
    def __init__(self, nome:str):
        self.__nome=nome
    
    def get_nome(self)->str:
        return self.__nome
    
    def __str__(self)->str:
        return self.__nome

class Mercado:
    def __init__(self, qtd_caixas:int):
        self.__caixas=list[Pessoa|None]=[]
        self.__espera =list[Pessoa]=[]
        
    def __str__(self):
        return f"[caixas:{self.__caixas}:espera:{self.__espera}]"
