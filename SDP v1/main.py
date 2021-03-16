
from Data import DATA
from Node import NODE
from User import USER


#----------creation du graph--------------------------------------------------------------------- 
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


node_list[4].addLNodeVoisin(node_list[3])
node_list[4].addLNodeVoisin(node_list[0])

user_list[0].addNode(node_list[2])

user_list[1].addNode(node_list[1])

user_list[2].addNode(node_list[0])

user_list[3].addNode(node_list[3])

user_list[4].addNode(node_list[4])

user_list[5].addNode(node_list[4])

#----------------------------------------------------------------------------------- 

#functionto get empty nodes from a list of nodes
def get_empty_nodes(node_list):
    empty_nodes=[]
    for node in node_list:
        if node.getLdonneesSL() == None:
            empty_nodes.append(node)
    return empty_nodes

#give  every user  a systemnode wich contains the first data he needs
for user in user_list:
    if user.getNoeudSystemeaccessible() !=None:
        node_system=user.getNoeudSystemeaccessible()
        
        #give the first node the first data 
        if user.getNotStockedData() !=[]:
            node_system.setLdonneesSL(user.getNotStockedData()[0])
            user.addStockedData(user.getLdonneesInteret()[0])

        
#give every systemnode  a nodevoisine that contains a data of the same user if it's empty
for user in user_list:
        node_system=user.getNoeudSystemeaccessible()
        
        if user.getNotStockedData() !=[]:
            empty_node_voisin=get_empty_nodes(node_system.getLNodeVoisin())
            
            if empty_node_voisin !=[]:
                empty_node_voisin[0].setLdonneesSL(user.getNotStockedData()[0])
                user.addStockedData(user.getNotStockedData()[0])
                #print('the empty node voisin  of ',node_system.getId(),' is ',empty_node_voisin[0].getId())
                #print(i,'   ',empty_node_voisin[0].getLdonneesSL())


#distribute the rest of data 
empty_nodes=get_empty_nodes(node_list)
for user in user_list:  
    
    if user.getNotStockedData() !=[]:
        for i in user.getNotStockedData():
            empty_nodes[0].setLdonneesSL(i)
            empty_nodes.remove(empty_nodes[0])
            user.addStockedData(user.getLdonneesInteret()[0])

for i in node_list:
    print ('Node : ',i.getId(),'contains the data ',i.getLdonneesSL())
    
            