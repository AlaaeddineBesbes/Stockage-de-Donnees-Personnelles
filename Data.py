class DATA:
    #id is a unique integer and taille is an integer

    def __init__(self,id,taille):
        self.id = id
        self.taille=taille

    def getId(self):
        return self.id

    def getTaille(self):
        return self.taille