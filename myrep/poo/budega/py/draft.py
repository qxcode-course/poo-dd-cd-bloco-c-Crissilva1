class Pessoa:
    def __init__(self, nome:str):
        self.__nome=nome
    
    def get_nome(self)->str:
        return self.__nome
    
    def __str__(self)->str:
        return self.__nome

class Mercado:
    def __init__(self, qtd_caixas:int=0):
        self.__caixas:list[Pessoa|None]=[None] * qtd_caixas
        self.__espera :list[Pessoa]=[]
        
    def __str__(self):
        caixas=", ".join(["-----" if elem is None else str(elem) for elem in self.__caixas])
        espera= ", ".join([str (elem)for elem in self.__espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    def chegar(self,pessoa:Pessoa)->None:
        self.__espera.append(pessoa)

    def chamar_Cliente(self, index:int)->None:
        if index <0 or index >= len(self.__caixas):
            print ("fail: caixa inexistente")
            return
        if self.__caixas[index]is not None:
            print("fail: caixa ocupado")
            return
        if len(self.__espera)==0:
            print ("fail: sem clientes")
            return
        self.__caixas[index]=self.__espera[0]
        del self.__espera[0]

    def finalizar(self, index:int)->Pessoa| None:
        if index < 0 or index >=len(self.__caixas):
            print("fail: caixa inexistente")
            return
        if self.__caixas[index] is None:
            print("fail: caixa vazio")
        self.__caixas[index]=None
        return 

    def sair_fila (self, nome:str)->Pessoa|None:
        for i, pessoa in enumerate (self.__espera):
            if pessoa.get_nome() == nome:
                aux=self.__espera[i]
                del self.__espera[i]
                return aux
    
    def Furar_fila(self,nome:str)->Pessoa |None:
          if len(self.__espera) == 0:
            print ("fail: sem clientes")
            return
          for i, pessoa in enumerate(self.__espera):
              if pessoa.get_nome() == nome:
                  aux=self.__espera[i]
                  del self.__espera[i]
                  self.__espera = [pessoa] + self.__espera
                  return aux
              
        





def main():
    mercado=Mercado()
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(mercado)
        elif args[0]=="init":
          qtd_caixas=int(args[1])
          mercado=Mercado(qtd_caixas)
        elif args [0]=="arrive":
            nome=str(args[1])
            pessoa=Pessoa(nome)
            mercado.chegar(pessoa)
        elif args [0]=="call":
            index=int(args[1])
            mercado.chamar_Cliente(index)
        elif args [0]=="finish":
            index=int(args[1])
            mercado.finalizar(index)


main()





