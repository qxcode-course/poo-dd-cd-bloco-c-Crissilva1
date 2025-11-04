class Criança:
    def __init__(self, nome:str, idade:int):
        self.__nome=nome
        self.__idade=idade

    def get_nome(self)->str:
        return self.__nome
    def get_idade(self)->int:
        return self.__idade
    
    def set_idade(self,idade:int)->None:
        self.__idade = idade
    def set_nome(self, nome:str)->None:
        self.__nome=nome


    def __str__(self):
        return f"[{self.__nome}:{self.__idade}]"
    
class Trampolim:
    def __init__(self,capacidade:int=0):
        self.__brincando:list[Criança|None]=[None] * capacidade
        self.__espera:list[Criança]=[]

    def __trampolim__(self):
        brincando=", ".join("[]" if elem is None else str(elem) for elem in self.__brincando)

