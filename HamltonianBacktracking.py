# Shivam Arora
# 101403169
# Assignment 6
# Hamiltonian path/circuit
# COE7
from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[v].append(u)
        self.graph[u].append(v)

    def checkHamiltonian(self):
        path = []
        for i in range(self.V):
            path.append(i)
            self.checkHamiltonianUtil(path)
            path.pop()

    def checkHamiltonianUtil(self,path):
        if path[-1]==path[0] and len(path)==self.V+1:
            print path, " ~~~~~ Hamiltonian circuit "
        elif len(path) == self.V:
            print path, " -----> Hamiltonian path  "

        for index, adjacent in enumerate(self.graph[path[-1]]):
            if adjacent not in path or (len(path)==self.V and adjacent == path[0]):
                path.append(adjacent)
                self.checkHamiltonianUtil(path)
                path.pop()






#########################################################################################################
                                                # MAIN
##########################################################################################################

x = int(raw_input("enter number of vertices"))

g = graph(x)
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(2,3)
# g.addEdge(3,4)
# g.addEdge(0,4)

u,v = raw_input("enter edges").strip().split()
u,v = int(u),int(v)
while v!=-1 and u!=-1:
    g.addEdge(u,v)
    u,v = raw_input("enter edges").strip().split()
    u,v = int(u),int(v)



g.checkHamiltonian()






