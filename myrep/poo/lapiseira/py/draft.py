class Grafite:
    def __init__(self, calibre:float, dureza:str , tamanho:int=0):
        self.__calibre:float=calibre
        self.__dureza:str=dureza
        self.__tamanho:int=tamanho

    def consumodeFolha(self)->int:
        gasto={"HB":1, "2B":2, "4B":4, "6B":6}[self.__dureza]
        self.__tamanho -=gasto
        return self.__tamanho
    
    def get_calibre(self)->float:
        return self.__calibre
    
    def get_dureza(self)->str:
        return self.__dureza
    
    def get_tamanho(self)->int:
        return self.__tamanho
    
    def set_tamanho(self, tamanho:int)->None:
        self.__tamanho=tamanho
    
    def __str__(self)->str:
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"
    
class Lapiseira:
    def __init__(self, calibre:float):
        self.__calibre:float=calibre
        self.__ponta:Grafite|None=None
        self.__tambor:list[Grafite]=[]

    def set_tambor(self,tambor:list):
        self.__tambor=tambor

    def get_tambor(self)->str:
        return self.__tambor
    
    def existeGrafite(self)->bool:
        if self.__ponta==None:
          return False
        if self.__ponta is not None:
          return True
        
    def inserir(self,grafite:Grafite)->bool:
        if grafite.get_calibre()!= self.__calibre:
            print("fail: calibre incompatível")
            return False
        self.__tambor.append(grafite)
        return True
    
    def puxar(self)->bool:
        if self.__ponta is not None:
            print("fail: ja existe grafite no bico")
            return False
        if len(self.__tambor)==0:
            return False
        self.__ponta=self.__tambor.pop(0)
        return True
    
    def remover(self)->Grafite|None:
        aux=self.__ponta
        self.__ponta=None
        return aux
    
    def __str__(self)->str:
        ponta_str="[]" if self.__ponta is None else str(self.__ponta)
        tambor_str="".join(str(elem)for elem in self.__tambor)
        return f"calibre: {self.__calibre}, bico: {ponta_str}, tambor: <{tambor_str}>"
    
    def EscreverPagina(self)->None:
        if self.__ponta ==None:
            print("fail: nao existe grafite no bico")
            return
        
        gasto={"HB":1, "2B":2, "4B":4, "6B":6}[self.__ponta.get_dureza()]

        if self.__ponta.get_tamanho()<=10:
            print("fail: tamanho insuficiente")
            return
        
        if self.__ponta.get_tamanho()-gasto<10:
            self.__ponta.set_tamanho(10)
            print ("fail: folha incompleta")
            return
        
        self.__ponta.consumodeFolha()

def main():
    lapiseira=Lapiseira(" ")
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(lapiseira)
        elif args[0]=="init":
             calibre=float(args[1])
             lapiseira=Lapiseira(calibre)
        elif args[0]=="insert":
            calibre=float(args[1])
            dureza=str(args[2])
            tamanho=int(args[3])
            grafite=Grafite(calibre,dureza,tamanho)
            lapiseira.inserir(grafite)
        elif args[0]=="pull":
            lapiseira.puxar()
        elif args[0]=="remove":
            lapiseira.remover()
        elif args[0]=="write":
            lapiseira.EscreverPagina()


main()