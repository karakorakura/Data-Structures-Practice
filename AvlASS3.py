# Shivam Arora
# 101403169
# Assignment 3
# Avl tree
# COE7


class Node:
    def __init__(self,data=None,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent
        self.height=0
                # 0 for self -1 for None
    def printNode(self):
        print "[",self.data,
        if self.left != None : print "l%s"%self.left.data,
        if self.right != None : print "r%s"%self.right.data ,
        if self.parent != None : print "p%s"%self.parent.data ,"",
        print "h%s"%self.height,
# Global
HeightTolerance = 2;

class Avl:
    def __init__(self,root=None):
        self.root=root

    def preorder(self,node=None):
        if node == None: node=self.root
        if node.left!=None: self.preorder(node.left)
        # print " ",node.data," ",
        node.printNode()
        if node.right!=None: self.preorder(node.right)

    # tell height of node
    def getHeight(self,node):
        if node==None:
            return -1
        else :
            return node.height

    def getBalanceVector(self,node):
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self,node):
        r = node.right
        node.right = r.left
        r.left=node
        if node.parent:
            if node==node.parent.left:
                node.parent.left=r
            elif node==node.parent.right:
                node.parent.right=r

        r.parent=node.parent
        if r.parent==None:self.root=r
        node.parent=r
        node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
        return r


    def rightRotate(self,node):
        l = node.left
        node.left = l.right
        l.right=node
        if node.parent:
            if node==node.parent.left:
                node.parent.left=l
            elif node==node.parent.right:
                node.parent.right=l

        l.parent=node.parent
        if l.parent==None:self.root=l
        node.parent=l
        node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
        return l

# balance height upwards
    def balanceUpwards(self,node):
        print "balancing ",node.data
        node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
        # check balnce vector left - right if it gets unbalanced then balance it
        balanceVector = self.getBalanceVector(node)
        if balanceVector <=-2:
            print "right high"
            # right high
            balanceVectorRight = self.getBalanceVector(node.right)
            if balanceVectorRight <=0:    #right high <0
                print "right right"
                # right right
                node = self.leftRotate(node)
                # new node change

            else:
                print "right left"
                # right left
                self.rightRotate(node.right)
                node = self.leftRotate(node)
        elif balanceVector>=2:
            print "left high"
            # left high
            balanceVectorLeft = self.getBalanceVector(node.left)
            if balanceVectorLeft >=0:   #left high >0
                # left left
                node = self.rightRotate(node)
            else:
                # right left
                self.leftRotate(node.left)
                node = self.rightRotate(node)


        if node != self.root and node!=None :
            print " calling balance"
            self.balanceUpwards(node.parent)


# Insertion At Node
    def insertAtNode(self,data,node):
        if data<=node.data:
            if node.left==None:
                print "inserting as left of",node.data
                node.left=Node(data)
                # updating parameters after insertion
                node.left.parent=node
                node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
                self.balanceUpwards(node)

            else:
                self.insertAtNode(data,node.left)
        else:
            if node.right==None:
                print "inserting as right of",node.data
                node.right=Node(data)
                # updating parameters after insertion
                node.right.parent=node
                node.height=max(self.getHeight(node.left),self.getHeight(node.right))+1
                self.balanceUpwards(node)

            else:
                self.insertAtNode(data,node.right)


    # Insertion start
    def insert(self,data=None):
        if self.root==None:
            self.root=Node(data)
        else:
            self.insertAtNode(data,self.root)

    # Search element


    # Deletion start unfinished
    def delete(self,data):
        pass

    ### main code test code below

avlTree = Avl()
x = 'y'
print " enter lements and n to stop "
x = raw_input('')
while x!='n':
    avlTree.insert(int(x))
    avlTree.preorder()
    x = raw_input('')


avlTree.preorder()
