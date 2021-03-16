class USER:
    #id is a unique integer
    #LdonneesInteret is a list of data ids
    #NoeudSystemeaccessible is a list of nodesysteme ids
    def __init__(self,id,LdonneesInteret=[],NoeudSystemeaccessible=None):
        self.id = id
        self.LdonneesInteret=sorted(LdonneesInteret)
        self.NoeudSystemeaccessible=NoeudSystemeaccessible
        self.notStockedData=sorted(LdonneesInteret)
    
    def getId(self):
        return self.id

    def getLdonneesInteret(self):
        return self.LdonneesInteret

    def getNoeudSystemeaccessible(self):
        return self.NoeudSystemeaccessible


    def setLdonneesInteret(self,LdonneesInteret):
        self.LdonneesInteret=LdonneesInteret

    def setNoeudSystemeaccessible(self,NoeudSystemeaccessible):
        self.NoeudSystemeaccessible=NoeudSystemeaccessible

    def addNode(self,node):
        self.NoeudSystemeaccessible=node
    
    def getNotStockedData(self):
        return self.notStockedData

    def addStockedData(self,data):
        if data in self.notStockedData:
            self.notStockedData.remove(data)