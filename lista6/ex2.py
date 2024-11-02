#Grafo por lista de adjascência
class vert():
    def __init__(self,name,valor=None):
        self.valor = valor
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
class grafo():
    def __init__(self,list_vert):
        self.lv = list_vert
        self.edge = {vert : [] for vert in self.lv}
    
    def __str__(self):
        stri = ""
        for vert in self.edge.keys():
            stri += vert.name + ":"
            stri += " " + "".join(str([conex for conex in self.edge[vert]]))
            stri += "\n"
        return stri
        
    def adjascent(self,x,y):
        if y in self.edge[x]:
            return True
        if x in self.edge[y]:
            return True
        return False

    def neighbors(self,x):
        lista_v = []
        for i in self.edge[x]:
            lista_v.append(i)
        return lista_v

    def add_vertex(self,x):
        if x in self.lv:
            return False
        else:
            self.edge[x] = []

            return True

    
    def remove_vertex(self,x):
        if x in self.edge:
            del self.edge[x]

            for vert in self.edge.keys():
                if x in self.edge[vert]:
                    self.edge[vert].remove(x)
            return True
        return False
    
    def add_edge(self,x,y):
        if y in self.edge[x]:
            return False
        else:
            self.edge[x].append(y)
            return True
    
    def remove_edge(self,x,y):
        if y in self.edge[x]:
            self.edge[x].remove(y)
            return True
        else:
            return False
    
    @staticmethod
    def get_vertex_value(x):
        return x.valor
    
    @staticmethod
    def set_vertex_value(x, new_valor):
        x.valor = new_valor


def bfs(grafo:grafo, vert_ini:vert) -> list:
    percorridos = []
    fila = [vert_ini]
    while fila:
        vert_atual = fila.pop(0)
        if vert_atual not in percorridos:
            percorridos.append(vert_atual)
            for i in grafo.neighbors(vert_atual):
                if i not in percorridos:
                    fila.append(i)
    return percorridos

        
def busca_propriedade(grafo:grafo,value) -> vert:
    lista_vert = grafo.edge.keys()
    visitados = []
    tops = []
    for vert in lista_vert:
        if vert not in visitados:
            fila = [vert]
            while fila:
                vert_atual = fila.pop(0)
                if vert_atual.valor == value:
                    tops.append(vert_atual)
                if vert_atual not in visitados:
                    visitados.append(vert_atual)
                    for i in grafo.neighbors(vert_atual):
                        if i not in visitados:
                            fila.append(i)
    return tops    


A = vert("A",1)
B = vert("B",1)
C = vert("C",0)
grafo1  = grafo([A,B,C])

print(busca_propriedade(grafo1,0))