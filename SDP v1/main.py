
from Data import DATA
from Node import NODE
from User import USER


def getElementById(element_list,id):
    for i in element_list:
        if i.getId()==id:
            return i

data_list=[DATA(1,25),DATA(2,30),DATA(3,35),DATA(4,30),DATA(5,15),DATA(6,40),DATA(7,10),DATA(8,35)]
user_list=[USER(1,[1,2]),USER(2,[4,5]),USER(3,[3]),USER(4),USER(5),USER(6)]
node_list=[NODE(1,40),NODE(2,40),NODE(3,50),NODE(4,40),NODE(5,50)]

node_list[0].addUser(user_list[2])
node_list[0].addLNodeVoisin(node_list[1])
node_list[0].addLNodeVoisin(node_list[4])

node_list[1].addUser(user_list[1])
node_list[1].addLNodeVoisin(node_list[0])
node_list[1].addLNodeVoisin(node_list[2])

node_list[2].addUser(user_list[0])
node_list[2].addLNodeVoisin(node_list[1])
node_list[2].addLNodeVoisin(node_list[3])

node_list[3].addUser(user_list[3])

node_list[3].addLNodeVoisin(node_list[2])
node_list[3].addLNodeVoisin(node_list[4])

#node_list[4].addUser(user_list[4])
#node_list[4].addUser(user_list[5])
node_list[4].addLNodeVoisin(node_list[3])
node_list[4].addLNodeVoisin(node_list[0])

user_list[0].addNode(node_list[2])
user_list[1].addNode(node_list[1])
user_list[2].addNode(node_list[0])
user_list[3].addNode(node_list[3])
user_list[4].addNode(node_list[4])
user_list[5].addNode(node_list[4])
i=0

def get_empty_nodes(node_list):
    empty_nodes=[]
    for node in node_list:
        if node.getLdonneesSL() == None:
            empty_nodes.append(node)
    return empty_nodes


for user in user_list:
    if user.getNoeudSystemeaccessible() !=None:
        #create the node and the data list for every user 
        node_system=user.getNoeudSystemeaccessible()
        
        #give the first node the first data 
        if user.getNotStockedData() !=[]:
            node_system.setLdonneesSL(user.getNotStockedData()[0])
            user.addStockedData(user.getLdonneesInteret()[0])
            i+=1
            print(i,'  ' ,node_system.getLdonneesSL())

        
#now every user has a systemnode wich contains the first data he needs
for user in user_list:
        node_system=user.getNoeudSystemeaccessible()
        
        if user.getNotStockedData() !=[]:
            empty_node_voisin=get_empty_nodes(node_system.getLNodeVoisin())
            
            if empty_node_voisin !=[]:
                empty_node_voisin[0].setLdonneesSL(user.getNotStockedData()[0])
                user.addStockedData(user.getNotStockedData()[0])
                #print('the empty node voisin  of ',node_system.getId(),' is ',empty_node_voisin[0].getId())
                #print(i,'   ',empty_node_voisin[0].getLdonneesSL())
#now every systemnode has a nodevoisine that contains a data of the same user if it's empty


empty_nodes=get_empty_nodes(node_list)
for user in user_list:  
    
    if user.getNotStockedData() !=[]:
        for i in user.getNotStockedData():
            print(user.getNotStockedData())
            empty_nodes[0].setLdonneesSL(i)
            i+=1
            print(i,'   ',empty_nodes[0].getLdonneesSL())
            empty_nodes.remove(empty_nodes[0])
            user.addStockedData(user.getLdonneesInteret()[0])

for i in node_list:
    print (i.getId(),'--',i.getLdonneesSL())
    
            



'''
for node in node_list:
    print(node.getLUsers()[0].getLdonneesInteret())
    if node.getLUsers()!= [] and len(node.getLUsers()[0].getLdonneesInteret())>1 :
        node_user=node.getLUsers()[0]
        Node_voisin_empty=empty_nodes(node.getLNodeVoisin())
        print( Node_voisin_empty)
        if Node_voisin_empty!=[]:
            print(node_user.getLdonneesInteret()[1])
            Node_voisin_empty[0].setLdonneesSL(node_user.getLdonneesInteret()[1])



for user in user_list:
    node = user.getNoeudSystemeaccessible()
    yes=len(user.getLdonneesInteret())>2
    if node!=None and yes :
        left_empty_nodes=empty_nodes(node_list)
        for i in range(len(user.getLdonneesInteret()[2:])):
            left_empty_nodes[i].setLdonneesSL(user.getLdonneesInteret()[i+2])

            
def NUD(data_list,user_list,node_list):
    nodeNumber=0
    for user in user_list:
        print(nodeNumber)
        if nodeNumber >= len(node_list):
            break
        userDataListID=sorted(user.getLdonneesInteret())
        user.setNoeudSystemeaccessible(getElementById(node_list,nodeNumber))
        if userDataListID != []:
            for dataID in userDataListID:
                if nodeNumber >= 6:
                    break
                node_list[nodeNumber].setLdonneesSL(node_list[nodeNumber].getLdonneesSL().append(dataID))
                if not(user.getId in node_list[nodeNumber].getLUsers()):
                    node_list[nodeNumber].setLUsers(node_list[nodeNumber].getLUsers().append(user.getId()))
                nodeNumber+=1
                
    for i in node_list:
        print(i.getLdonneesSL(),'  ',i.getLUsers())
NUD(data_list,user_list,node_list)       

'''                


        
    
 
'''
    for i in range(9):
        data_list.append(Data(i+1,randint(25,40)))
        user_list.append(User(i+1))
        Node_list.append(Node(i+1,randint(50,80)))
    for i in data_list:
        user=getElementById(randint(0,9))
        userdlist=user.getLdonneesInteret()
        userdlist.append(i.getId)
        user.setLdonneesInteret(userdlist)

    for i in user_list:  
        pass
'''