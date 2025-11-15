class Cliente:
    def __init__(self, id:str, telefone:int):
        self.__telefone:int = telefone
        self.__id :str = id

    def get_telefone(self)->int:
        return self.__telefone
    
    def get_id(self)->str:
        return self.__id
    
    def set_telefone(self, telefone:int)->None:
        self.__telefone = telefone

    def set_id(self, id:str)->None:
        self.__id = id

    def __str__(self):
        return f"{self.__id}:{self.__telefone}"
    
class Cinema:
    def __init__(self, capacidade:int=0):
        self.__capacidade:int = capacidade
        self.__assentos:list[Cliente|None]=[None] * capacidade

    def __str__(self):
        return f"["+" ".join(str(elem) if elem is not None else "-" for elem in self.__assentos)+ "]"

    def __search(self, id:str)->int:
        for i, cliente in enumerate(self.__assentos):
            if cliente is not None and cliente.get_id()==id:
                return i
        return -1


    def reserva(self,id:str, telefone:int, index:int):
        if index < 0 or index >= len(self.__assentos):
            print ("fail: cadeira nao existe")
            return
        if self.__assentos[index] is not None:
            print ("fail: cadeira ja esta ocupada")
            return
        for cliente in self.__assentos:
            if cliente is not None and cliente.get_id()==id:
                print("fail: cliente ja esta no cinema")
                return
        self.__assentos[index]=Cliente(id, telefone)
    
    def cancela(self, id:str)->bool:
        index=self.__search(id)
        if index== -1:
            print("fail: cliente nao esta no cinema")
            return False
        self.__assentos[index]=None
        return True

    

    
def main():
    cinema=Cinema(0)
    while True:
        line:str=input()
        print("$"+ line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(cinema)
        elif args[0]=="init":
            capacidade=int(args[1])
            cinema=Cinema(capacidade)
        elif args[0]=="reserve":
            id=args[1]
            telefone=int(args[2])
            index=int(args[3])
            cinema.reserva(id,telefone,index)
        elif args[0]=="cancel":
            id=str(args[1])
            cinema.cancela(id)

        

main()













    