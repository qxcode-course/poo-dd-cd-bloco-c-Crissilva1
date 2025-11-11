class Cliente:
    def __init__(self, id:str, telefone:int):
        self.__telefone:int = telefone
        self.__id :str = id

    def get_telefone(self)->int:
        return self.__telefone
    
    def get_id(self)->str:
        return self.__id
    
    def set_telefone(self, telefone:int)->int:
        self.__telefone = telefone

    def set_id(self, id:str)->str:
        self.__id = id

    def __str__(self):
        return f"{self.__telefone}:{self.__id}"
    
class Cinema:
    def __init__(self, capacidade:int):
        self.__capacidade:int = capacidade
        self.__asssentos:list[Cliente|None]=[]

    def __search(self, nome: str) -> int:
        for i, nome in enumerate(self.__assentos):
            

    def __verificarIndice(self, index : int)->int:

















    