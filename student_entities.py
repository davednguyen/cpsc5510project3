# # # """
# # # CPSC 5510, Seattle University, Project #3
# # # :Author: student # FIXME fill in _your_name
# # # :Version: s23
# # # """

# # # # YOU MAY NOT ADD ANY IMPORTS
# # # from entity import Entity
# # # from student_utilities import to_layer_2


# # # def common_init(self):
# # #     """
# # #     You may call a common function like this from your individual __init__ 
# # #     methods if you want.
# # #     """
# # #     pass  # FIXME (optional)


# # # def common_update(self, packet):
# # #     """
# # #     You may call a common function like this from your individual update 
# # #     methods if you want.
# # #     """
# # #     pass  # FIXME


def common_link_cost_change(self, to_entity, new_cost):
    """
    You may call a common function like this from your individual 
    link_cost_change methods if you want.
    Note this is only for extra credit and only required for Entity0 and 
    Entity1.
    """
    pass  # FIXME (optional)


# # # class Entity0(Entity):
# # #     """Router running a DV algorithm at node 0"""
# # #     pass  # FIXME


# # # class Entity1(Entity):
# # #     """Router running a DV algorithm at node 1"""
# # #     pass  # FIXME


# # # class Entity2(Entity):
# # #     """Router running a DV algorithm at node 2"""
# # #     pass  # FIXME


# # # class Entity3(Entity):
# # #     """Router running a DV algorithm at node 3"""
# # #     pass  # FIXME
# # """
# CPSC 5510, Seattle University, Project #3
# :Author: David Nguyen
# :Version: s23
# """

from entity import Entity
from student_utilities import to_layer_2


Infinity = float('inf')#set unreachable nodes
Entities = 4 #total 4 entities 

# def printOut(node):
#     print('entity ' + str(node) + ': initializing')
#     print('node:' + str(node))

##
#private helper method to support for printout
#follow printout format as in example of the requirements
##
def printOut(node, distance_table, costs):
    print(f"entity {node}: initializing")
    print(f"node: {node}")
    print(costs)
    # for row in distance_table:
    #     print(row)
    for i in range(3):
        print(distance_table[i])

##
# private method return the cost of each note to the all its neighbors
# provide distant vector costs of each node for calculation
##
def node_neighbors(node_id):
    link_costs = {
        #cost from node 0, 1, 2, 3 to others
        0: {1: 1, 2: 3, 3: 7},
        1: {0: 1, 2: 1},
        2: {0: 3, 1: 1, 3: 2},
        3: {0: 7, 2: 2}
    }
    #return list of costs for each node ID
    return link_costs[node_id]

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
#method to setup link costs
#initialzie distance table
##
def common_init(self):
    # # #     """
    # # #     You may call a common function like this from your individual __init__ 
    # # #     methods if you want.
    # # #     """
    # # #     pass  #  (optional)

    # #initialize list of nodes (currently)
    # self.min_costs = [Infinity] * Entities
    # #set starting cost = 0 where cost of a node to itself
    # self.min_costs[self.node] = 0 
    
    # #allCost = node_neighbors(self.node);
    # cost = []
    # cost.append(0)
    # #get list all costs to its neghbors 
    # self.neighbors = node_neighbors(self.node)    

    # for dest in self.neighbors:
    # #for dest in range(Entities):
    #     #print("next destination: " + str(dest))
    #     self.distance_table[dest][dest] = self.neighbors[dest]
    #     self.min_costs[dest] = self.neighbors[dest]
    #     #cost.append(allCost[dest])
    # #call printout helper mesthod to display the steps
    # printOut(self.node, self.distance_table, self.min_costs)

    # # Send initial min_costs to neighbors
    # for neighbor in self.neighbors:
    #     to_layer_2(self.node, neighbor, self.min_costs)
    print("entity: initializing".format(self.current))
    Entity.__init__(self)
    self.node = self.current
    for i in range(Entities):
        self.distance_table[self.node][i] = self.cost[i]
    print(self.__str__())
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
    # updated = False
    # src = packet.src

    # for dest in range(Entities):
    #     if dest == self.node:
    #         continue
    #     cost_to_src = self.neighbors.get(src, Infinity)
    #     new_cost = cost_to_src + packet.mincost[dest]
    #     #print("new common update...")

    #     if new_cost < self.distance_table[dest][src]:
    #         self.distance_table[dest][src] = new_cost
    #         updated = True

    # if updated:
    #     for dest in range(Entities):
    #         self.min_costs[dest] = min(self.distance_table[dest])
    #     #print("updated....")
    #     for neighbor in self.neighbors:
    #         to_layer_2(self.node, neighbor, self.min_costs)
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
        print("changes based on update")
        print(self.__str__())
        print("sending mincost update to neighbors")
        print()
        for i in range(Entities):
            if i != self.node and self.cost[i] != Infinity:
                to_layer_2(self.node, i, self.sendcost)
    else:
        print("no change in node{}, so nothing to do".format(self.node))
        print(self.__str__())


class Entity0(Entity):
    # # #     """Router running a DV algorithm at node 0"""
    def __init__(self):
        super().__init__()
        self.current = 0
        self.node = 0
        self.cost = travel_cost(0)
        #print(travel_cost(0))
        self.sendcost = travel_cost(0)
        #printOut(0)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit


class Entity1(Entity):
    # # #     """Router running a DV algorithm at node 1"""
    def __init__(self):
        super().__init__()
        self.node = 1
        self.current = 1
        self.cost = travel_cost(1)
        #print(travel_cost(1))
        self.sendcost = travel_cost(1)
        #printOut(1)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit


class Entity2(Entity):
    # # #     """Router running a DV algorithm at node 2"""
    def __init__(self):
        super().__init__()
        self.node = 2
        self.current = 2
        self.cost = travel_cost(2)
        #print(travel_cost(2))
        self.sendcost = travel_cost(2)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass # Optional for extra credit


class Entity3(Entity):
    # # #     """Router running a DV algorithm at node 3"""
    def __init__(self):
        super().__init__()
        self.node = 3
        self.current = 3
        self.cost = travel_cost(3)
        #print(travel_cost(3))
        self.sendcost = travel_cost(3)
        #printOut(3)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass # Optional for extra credit
