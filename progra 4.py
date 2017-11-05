#Progra 4 Lenguajes

class Bone:
    def __init__(self, ID, pip1, pip2):
        self.ID = ID
        self.pip1 = pip1
        self.pip2 = pip2

class ListaBones:
    def __init__(self):
        self.lista = []

    def agregarBone(self,bone):
        self.lista.append(bone)

    def buscarBone(self, pip1, pip2):
        for bone in self.lista:
            if (bone.pip1 == pip1 and bone.pip2 == pip2):
                return bone
            if (bone.pip2 == pip1 and bone.pip1 == pip2):
                return bone
        return None

class ListaMapasPips:
    def __init__(self):
        self.lista_mapas = []

    def insertarMapa(self, mapa):
        self.lista_mapas.append(mapa)

    def resolverLista(self):
        for i in range(len(self.lista_mapas)):
            print("Conjunto #", end = "")
            print(i+1, end = "")
            print(":")
            self.lista_mapas[i].imprimir()
            print("Mapas resultantes del conjunto #", end = "")
            print(i+1, end = "")
            print(".")
            self.lista_mapas[i].resolverMapa()
            print ("Hay", self.lista_mapas[i].soluciones, "solución(es) para el conjunto #", end = "")
            print (i+1, end = "")
            print (".")
            print()

class MapaPips:
    def __init__(self, matriz):
        self.matriz = matriz
        self.mapa_bones = MapaBones()
        self.soluciones = 0

    def imprimir(self):
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz[0])):
                print(self.matriz[i][j], end = " ")
            print()
        print()

    def resolverMapa(self):
        global listaBones
        #aqui va todo el codigo de backtracking :)
        listaPos = self.mapa_bones.siguientesPares() 
        while(listaPos != []):
            if(not self.mapa_bones.hayCeros()):
                self.mapa_bones.imprimir()
                self.soluciones +=1
                return False
            else:
                x1 = listaPos[0][0][0]
                y1 = listaPos[0][0][1]
                x2 = listaPos[0][1][0]
                y2 = listaPos[0][1][1]
                
                bone = listaBones.buscarBone(self.matriz[x1][y1],self.matriz[x2][y2])
                if(bone != None):
                    if(not bone.ID in self.mapa_bones.utilizados):
                        self.mapa_bones.utilizados.append(bone.ID)
                        self.mapa_bones.matriz[x1][y1] = bone.ID
                        self.mapa_bones.matriz[x2][y2] = bone.ID
                        solu = self.resolverMapa()
                        if(solu):
                            return True
                        else:
                            del listaPos[0]
                            self.mapa_bones.utilizados.remove(bone.ID)
                            self.mapa_bones.matriz[x1][y1] = 0
                            self.mapa_bones.matriz[x2][y2] = 0
                    else:
                        del listaPos[0]
            
        return False

    
class MapaBones:
    def __init__(self):
        self.utilizados = []
        self.matriz = []
        for i in range (7):
            self.matriz.append([])
            for j in range (8):
                self.matriz[i].append(0)

    def quitarBone(self, id_bone):
        self.utilizados.remove(id_bone)
        for i in range (7):
            for j in range (8):
                if self.matriz[i][j] == id_bone: 
                    self.matriz[i][j] = 0

    def siguientesPares(self):
        respuestas = []
        for i in range (7):
            for j in range (8):
                if self.matriz[i][j] == 0:
                    if(j != 7):
                        if(self.matriz[i][j+1] == 0):
                            respuestas.append( ((i,j),(i,j+1)) )
                    if(i != 6):
                        if(self.matriz[i+1][j] == 0):
                            respuestas.append( ((i,j),(i+1,j)) )
                    return respuestas

    def hayCeros(self):
        for i in range (7):
            for j in range (8):
                if self.matriz[i][j] == 0:
                    return True
        return False

    def imprimir(self):
        for i in range (len(self.matriz)):
            for j in range (len(self.matriz[0])):
                if(self.matriz[i][j]>9):
                    print(self.matriz[i][j], end = " ")
                else:
                    print("",self.matriz[i][j], end = " ")
            print()
        print()

#crea e inserta los bones
listaBones = ListaBones()
ID = 1
for i in range (7):#pip1
    for j in range (i,7): #pip2
        bone = Bone(ID, i, j)
        listaBones.agregarBone(bone)
        ID +=1


#crea la lista de mapas pips
listaMapasPips = ListaMapasPips()

#crea un mapa pips



matriz = [ [5, 4, 3, 6, 5, 3, 4, 6],
           [0, 6, 0, 1, 2, 3, 1, 1],
           [3, 2, 6, 5, 0, 4, 2, 0],
           [5, 3, 6, 2, 3, 2, 0, 6],
           [4, 0, 4, 1, 0, 0, 4, 1],
           [5, 2, 2, 4, 4, 1, 6, 5],
           [5, 5, 3, 6, 1, 2, 3, 1] ]


mapa_pips = MapaPips(matriz)

listaMapasPips.insertarMapa(mapa_pips)

matriz = [ [4, 2, 5, 2, 6, 3, 5, 4],
           [5, 0, 4, 3, 1, 4, 1, 1],
           [1, 2, 3, 0, 2, 2, 2, 2],
           [1, 4, 0, 1, 3, 5, 6, 5],
           [4, 0, 6, 0, 3, 6, 6, 5],
           [4, 0, 1, 6, 4, 0, 3, 0],
           [6, 5, 3, 6, 2, 1, 5, 3] ]

mapa_pips = MapaPips(matriz)

listaMapasPips.insertarMapa(mapa_pips)

listaMapasPips.resolverLista()

