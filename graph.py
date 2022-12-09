from node import *
import numpy as np

def load(graph,indice):
    pass

class Graph(object):
    def __init__(self) -> None:
        self.edge_number = 0
        self.density = 0
        self.nodes = {}

    def __add_node__(self,node: int) -> None:
        self.nodes[node] = Node(node)
    
    def __add_edge__(self,config:list) -> None:
        if len(config) == 3:
            origin = config[0]
            destiny = config[1]
            value = config[2]
            #verificando existencia de nós
            for n in [origin,destiny]:
                if not n in self.nodes:
                    self.__add_node__(n)
            
            self.nodes[origin].addChild(self.nodes[destiny],value)
            self.nodes[destiny].addParent(self.nodes[origin],value)
            self.edge_number +=1
                
    def load(self,path:str) -> None:
        with open(path) as file:
            contents = file.readlines()
            for line in contents:
                self.__add_edge__([int(x) for x in line.split()])
