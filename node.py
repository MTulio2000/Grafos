class Node(object):
    def __init__(self,indice):
        self.child = []
        self.parents = []
        self.indice = indice

    def addChild(self,node,value)-> None:
        self.child.append((node,value))

    def addParent(self,node,value)-> None:
        self.parents.append((node,value))