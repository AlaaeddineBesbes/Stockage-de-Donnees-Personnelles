class NODE:
    #id is a unique integer
    #capaciteMemoire is an integer
    #ldonnesSL is a list of data ids
    #LUsers is a list of ids of (users)
    def __init__(self,id,capaciteMemoire,LdonneesSL=None,LUsers=[],LNodeVoisin=[]):
        self.id=id
        self.CapaciteMemoire=capaciteMemoire
        self.LdonneesSL=LdonneesSL
        self.LUsers=LUsers
        self.LNodeVoisin=[]

    def addUser(self,user):
        self.LUsers.append(user)

    def addLNodeVoisin(self,Node):
        self.LNodeVoisin.append(Node)

    def getId(self):
        return self.id

    def getCapaciteMemoire(self):
        return self.CapaciteMemoire

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

