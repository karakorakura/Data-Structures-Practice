# Shivam Arora
# 101403169
# Assignment 4
# Avl tree
# COE7

#GlObal
#degree
t=2;

class Node:
    def __init__(self,data=None,parent = None,pointers = None,leaf = True):
        self.keys = []
        self.pointers=[]
        self.keysLength = 0
        self.parent=parent
        self.leaf = leaf
        if data!=None :
            for d in data:
                self.keys.append(d)
                self.keysLength+=1

        if pointers!=None :
            for p in pointers:
                self.pointers.append(p)

    def search(self,data):
        i = 0
        while i < self.keysLength and data > self.keys[i]:
            i += 1

        if self.keys[i] == data:
            return self

        if self.leaf:
            return None

        return self.pointers[i].search(data)

    def insert(self,data,node1=None,node2=None):
        i = 0
        while i < self.keysLength and data > self.keys[i]:
            i += 1

        self.keys.insert(i,data)
        self.keysLength+=1
        if i < len(self.pointers) :
            self.pointers[i]=node1
        else:
            self.pointers.append(node1)

        self.pointers.insert(i+1,node2)




class Btree:
    def __init__(self,root=None):
        global t 
        self.degree=t
        self.maxKeyLength = self.degree*2 - 1
        self.minKeyLength = self.degree - 1
        # self.root=Node(root)
        self.root=None

    def printTree(self,node=None):
        if node==None:
            node= self.root

        if node.leaf:
            for key in node.keys:
                print key,
        else :
            i=0


            for key in node.keys:
                self.printTree(node.pointers[i])
                print key,
                i+=1
            self.printTree(node.pointers[i])

    def preorder(self,node=None):
        if node==None:
            node= self.root

        if node.leaf:
            for key in node.keys:
                print key,
        else :
            i=0
            for key in node.keys:
                print key,
                # printTree(pointers[i+1])
                i+=1



        pass

    def split(self,node=None):
        parent = node.parent
        #mid element keys[t-1]
        node1 = Node(data = node.keys[:t-1], pointers = node.pointers[:t] )
        node2 = Node(data = node.keys[t:], pointers = node.pointers[t+1:] )

        if parent==None:
            self.root = Node([node.keys[t-1]],pointers=[node1,node2],leaf=False)
            parent = self.root
            parent.leaf = False
        else :
            parent.insert(node.keys[t-1],node1,node2)

        node1.parent=parent
        node2.parent=parent

    #Insertion at node
    def insertAtNode(self,data,node):
        i = 0
        while i < node.keysLength and data > node.keys[i]:
            i += 1

        if node.leaf:
            node.insert(data)
            if node.keysLength>=2*t-1:
                self.split(node)

        else:
            self.insertAtNode(data,node.pointers[i])



    # Insertion start
    def insert(self,data=None):
        if self.root==None:
            self.root=Node([data])
        else:
            self.insertAtNode(data,self.root)

    # Search element


    # Deletion start unfinished
    def delete(self,data):
        pass

############################################## main code test code below

b =  Btree()
# b.insert(1)
# b.insert(2)
# b.insert(3)
# b.insert(4)
# b.insert(5)
# b.insert(6)
x=0
x=int(raw_input('enter value to insert -1 to exit'))
while x!=-1:
    b.insert(x)
    x=int(raw_input('enter value to insert -1 to exit'))


b.printTree();
# b.preorder();
