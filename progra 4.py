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
            if (bone.pip1 = pip1 and bone.pip2 = pip2):
                return bone
            if (bone.pip2 = pip1 and bone.pip1 = pip2):
                return bone
    return None

class MapaPips:
    def __init__(self, matriz):
        self.matriz = matriz 

class MapaBones:
    def __init__(self):
        self.utilizados = []
        self.matriz = []
        for i in range (7):
            self.matriz.append([])
            for j in range (8):
                self.matriz.append(0)

    def quitarBone(self, id_bone):
        self.utilizados.remove(id_bone)
        for i in range (7):
            for j in range (8):
                if self.matriz[i][j] == id_bone:
                    self.matriz[i][j] = 0

#crea e inserta los bones
listaBones = ListaBones()
ID = 1
for i in range (7):#pip1
    for j in range (i,7): #pip2
        bone = Bone(ID, i, j)
        listaBones.agregarBone(bone)
        ID +=1

print (len (listaBones.lista))
