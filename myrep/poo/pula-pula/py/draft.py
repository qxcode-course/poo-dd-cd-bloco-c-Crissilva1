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


    def __str__(self)->str:
        return f"{self.__nome}:{self.__idade}"
    
class Trampolim:
    def __init__(self,qtd_max:int=0):
        self.__brincando:list[Criança]=[] 
        self.__espera:list[Criança]=[]

    def __str__(self)->str:
        espera=", ".join(str(criança)for criança in reversed (self.__espera))
        brincando=", ".join(str(criança)for criança in reversed (self.__brincando))
        return f"[{espera}] => [{brincando}]"

    def inserir (self,criança:Criança)->None:
        self.__espera.append(criança)
    
    def mover_fila(self)->None:
       if len(self.__espera) >0:
          aux:Criança=self.__espera.pop(0)
          self.__brincando.append(aux)
       return

    def mover_brincando(self)->None:
        if len (self.__brincando) >0:
           aux=self.__brincando.pop(0)
           self.__espera.append(aux)
        return
    
    def remover_criança(self,criança:Criança, nome:str, idade:int)->None:
        for i, criança in enumerate(self.__espera):
            if criança.get_nome()==nome and criança.get_idade() ==idade:
                del self.__espera[i]
                return
            
        for i, criança in enumerate(self.__brincando):
            if criança.get_nome() == nome and criança.get_idade() == idade:
                del self.__espera[i]
                return
    
    def remover_da_lista(self, nome:str)->None:
        for i, criança in enumerate(self.__espera):
            if criança.get_nome()==nome:
                del self.__espera[i]
                return
            
        for i, criança in enumerate (self.__brincando):
            if criança.get_nome()==nome:
                del self.__brincando[i]
                return
            
        print(f"fail: {nome} nao esta no pula-pula")

def main():
    trampolim=Trampolim()
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(trampolim)
        elif args[0]=="arrive":
            nome=str(args[1])
            idade=int(args[2])
            criança=Criança(nome,idade)
            trampolim.inserir(criança)
        elif args[0]=="enter":
            trampolim.mover_fila()
        elif args[0] =="leave":
            trampolim.mover_brincando()
        elif args[0]=="remove":
            nome=str(args[1])
            trampolim.remover_da_lista(nome)
       
    
main()

     
        



