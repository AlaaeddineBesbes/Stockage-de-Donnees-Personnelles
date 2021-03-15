class NODE:
    #id is a unique integer
    #capaciteMemoire is an integer
    #ldonnesSL is a list of data ids
    #LUsers is a list of ids of (users)
    def __init__(self,id,capaciteMemoire,LdonneesSL=None,LUsers=[],LNodeVoisin=[]):
        self.id=id
        self.capaciteMemoire=capaciteMemoire
        self.LdonneesSL=LdonneesSL
        self.LUsers=LUsers
        self.LNodeVoisin=[]

    def addUser(self,user):
        self.LUsers.append(user)

    def addLNodeVoisin(self,Node):
        self.LNodeVoisin.append(Node)

    def getId(self):
        return self.id

    def getapaciteMemoire(self):
        return self.apaciteMemoire

    def getLdonneesSL(self):
        return self.LdonneesSL

    def getLUsers(self):
        return self.LUsers

    def getLNodeVoisin(self):
        return self.LNodeVoisin

    def setLdonneesSL(self,LdonneesSL):
        self.LdonneesSL=LdonneesSL

    def setLUsers(self,LUsers):
        self.LUsers=LUsers

    def fill_data(self,data=[]):
        data_filled=[]
        data_left=[]
        totalSize=0
        for i in data:
            totalSize=totalSize+i.getTaille
            if self.capaciteMemoire>=totalSize:
                data_filled.append(i.id)
            else:
                data_left.append(i)
        return (data_filled,data_left)
