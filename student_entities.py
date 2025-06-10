# # # """
# # # CPSC 5510, Seattle University, Project #3
# # # :Author: David Nguyen
# # # :Version: 
# # # """

# # # # YOU MAY NOT ADD ANY IMPORTS
from entity import Entity
from student_utilities import to_layer_2


def common_link_cost_change(self, to_entity, new_cost):
    """
    You may call a common function like this from your individual 
    link_cost_change methods if you want.
    Note this is only for extra credit and only required for Entity0 and 
    Entity1.
    """
    pass  # FIXME (optional)

Infinity = float('INF')#set unreachable nodes
Entities = 4 #total 4 entities 

##
#private helper method to support for printout
#follow printout format as in example of the requirements
##
def printOutCostInitalizing(node, distance_table):
    print(f"entity {node}: initializing")
    print(f"node: {node}")
    for i in distance_table:
       print(i)
    print()

##
#private method return cost of each node ID as in array
##
def travel_cost(node_id):
    # Set initial link costs based on node ID
    link_costs = {
        0: [0, 1, 3, 7],
        1: [1, 0, 1, Infinity],
        2: [3, 1, 0, 2],
        3: [7, Infinity, 2, 0]
    }
    return link_costs[node_id]

##
# print out changing parts
##
def printOut(change):
    print("changes based on update")
    print(change)
    print("sending mincost update to neighbors")
    print()

##
# print out no change notes
##
def printOutNote(node, selfNode):
    print("no change in node {}, so nothing to do".format(node))
    print(selfNode)
##
#method to setup link costs
#initialzie distance table
##
def common_init(self):
    # # #     """
    # # #     You may call a common function like this from your individual __init__ 
    # # #     methods if you want.
    # # #     """
    # # #     pass  #  (optional)    
    Entity.__init__(self)
    self.node = self.current
    for i in range(Entities):
        self.distance_table[self.node][i] = self.cost[i]
    #print out initalizing parts and costs
    printOutCostInitalizing(self.current, self.distance_table)

    for i in range(Entities):
        if i != self.node and self.distance_table[self.node][i] != Infinity:
            to_layer_2(self.node, i, self.sendcost)
    

##
#update method for delivery packet 
##
def common_update(self, packet):
    # # #     """
    # # #     You may call a common function like this from your individual update 
    # # #     methods if you want.
    # # #     """
    # # #     pass  #
    change = False
    srcnode = packet.src
    thisnode = packet.dest
    mincost = packet.mincost

    for i in range(Entities):
        if(self.distance_table[srcnode][i] > mincost[i]):
            self.distance_table[srcnode][i] > mincost[i]
    for j in range(Entities):
        temp = self.cost[srcnode] + mincost[j]
        self.distance_table[thisnode][j] = min(self.distance_table[thisnode][j], temp)
        if temp <self.sendcost[j]:
            change = True
            self.sendcost[j] = temp

    if change:
        #print out change
        printOut(self.__str__())
        for i in range(Entities):
            if i != self.node and self.cost[i] != Infinity:
                to_layer_2(self.node, i, self.sendcost)
    else:
        #print out no change note
        printOutNote(self.node, self.__str__())

##
# run cost for entity 0
##
class Entity0(Entity):
    # # #     """Router running a DV algorithm at node 0"""
    def __init__(self):
        super().__init__()
        self.current = 0
        self.node = 0
        self.cost = travel_cost(0)
        self.sendcost = travel_cost(0)
        common_init(self)

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit

##
# run cost for entity 1
##
class Entity1(Entity):
    # # #     """Router running a DV algorithm at node 1"""
    def __init__(self):
        super().__init__()
        self.node = 1
        self.current = 1
        self.cost = travel_cost(1)
        self.sendcost = travel_cost(1)
        common_init(self)

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit

##
# run cost for entity 2
##
class Entity2(Entity):
    # # #     """Router running a DV algorithm at node 2"""
    def __init__(self):
        super().__init__()
        self.node = 2
        self.current = 2
        self.cost = travel_cost(2)
        self.sendcost = travel_cost(2)
        common_init(self)

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass # Optional for extra credit

##
# run cost for entity 3
##
class Entity3(Entity):
    # # #     """Router running a DV algorithm at node 3"""
    def __init__(self):
        super().__init__()
        self.node = 3
        self.current = 3
        self.cost = travel_cost(3)
        self.sendcost = travel_cost(3)
        common_init(self)

    def update(self, packet):
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass # Optional for extra credit
