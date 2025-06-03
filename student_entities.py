# """
# CPSC 5510, Seattle University, Project #3
# :Author: student # FIXME fill in _your_name
# :Version: s23
# """

# # YOU MAY NOT ADD ANY IMPORTS
# from entity import Entity
# from student_utilities import to_layer_2


# def common_init(self):
#     """
#     You may call a common function like this from your individual __init__ 
#     methods if you want.
#     """
#     pass  # FIXME (optional)


# def common_update(self, packet):
#     """
#     You may call a common function like this from your individual update 
#     methods if you want.
#     """
#     pass  # FIXME


# def common_link_cost_change(self, to_entity, new_cost):
#     """
#     You may call a common function like this from your individual 
#     link_cost_change methods if you want.
#     Note this is only for extra credit and only required for Entity0 and 
#     Entity1.
#     """
#     pass  # FIXME (optional)


# class Entity0(Entity):
#     """Router running a DV algorithm at node 0"""
#     pass  # FIXME


# class Entity1(Entity):
#     """Router running a DV algorithm at node 1"""
#     pass  # FIXME


# class Entity2(Entity):
#     """Router running a DV algorithm at node 2"""
#     pass  # FIXME


# class Entity3(Entity):
#     """Router running a DV algorithm at node 3"""
#     pass  # FIXME
"""
CPSC 5510, Seattle University, Project #3
:Author: David Nguyen
:Version: s23
"""

from entity import Entity
from student_utilities import to_layer_2


INFINITY = float('inf')
NUM_ENTITIES = 4

# def printOut(node):
#     print('entity ' + str(node) + ': initializing')
#     print('node:' + str(node))

def printOut(node, distance_table, costs):
    print(f"entity {node}: initializing")
    print(f"node: {node}")
    print(costs)
    for row in distance_table:
        print(row)


def node_neighbors(node_id):
    link_costs = {
        #cost from node 0, 1, 2, 3 to others
        0: {1: 1, 2: 3, 3: 7},
        1: {0: 1, 2: 1},
        2: {0: 3, 1: 1, 3: 2},
        3: {0: 7, 2: 2}
    }
    return link_costs[node_id]


def common_init(self):
    
    self.min_costs = [INFINITY] * NUM_ENTITIES
    self.min_costs[self.node] = 0
    allCost = node_neighbors(self.node);
    cost = []
    cost.append(0)
    self.neighbors = node_neighbors(self.node)    

    for dest in self.neighbors:
        #print("next destination: " + str(dest))
        self.distance_table[dest][dest] = self.neighbors[dest]
        self.min_costs[dest] = self.neighbors[dest]
        cost.append(allCost[dest])
    printOut(self.node, self.distance_table, self.min_costs)
    #print(cost)
    # Send initial min_costs to neighbors
    for neighbor in self.neighbors:
        to_layer_2(self.node, neighbor, self.min_costs)


def common_update(self, packet):
    updated = False
    src = packet.src

    for dest in range(NUM_ENTITIES):
        if dest == self.node:
            continue
        cost_to_src = self.neighbors.get(src, INFINITY)
        new_cost = cost_to_src + packet.mincost[dest]
        #print("new common update...")

        if new_cost < self.distance_table[dest][src]:
            self.distance_table[dest][src] = new_cost
            updated = True

    if updated:
        for dest in range(NUM_ENTITIES):
            self.min_costs[dest] = min(self.distance_table[dest])
        #print("updated....")
        for neighbor in self.neighbors:
            to_layer_2(self.node, neighbor, self.min_costs)


class Entity0(Entity):
    def __init__(self):
        super().__init__()
        self.node = 0
        #printOut(0)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit


class Entity1(Entity):
    def __init__(self):
        super().__init__()
        self.node = 1
        #printOut(1)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass  # Optional for extra credit


class Entity2(Entity):
    def __init__(self):
        super().__init__()
        self.node = 2
        #printOut(2)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):

        pass


class Entity3(Entity):
    def __init__(self):
        super().__init__()
        self.node = 3
        #printOut(3)
        common_init(self)

    def update(self, packet):
        #print("called udpated method")
        common_update(self, packet)

    def link_cost_change(self, to_entity, new_cost):
        pass
