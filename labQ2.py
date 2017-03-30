class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

class Bst:
    def __init__(self,data=None):
        node = Node(data)
        self.root=node

    def insert(self,data,parent=None):

        if parent==None:parent=self.root
        node = Node(data)
        if self.root==None:self.root=node
        else:
            if data<parent.data:
                if parent.left==None:
                    parent.left=node
                else :
                    self.insert(data,parent.left)
            else :
                if parent.right==None:
                    parent.right=node
                else :
                    self.insert(data,parent.right)

    def inorder(self,node=None):
        if node==None:node=self.root
        if node.left!=None:self.inorder(node.left)
        print node.data
        if node.right!=None:self.inorder(node.right)

    def postorder(self,node=None):
        if node==None:node=self.root
        if node.left!=None:self.postorder(node.left)
        if node.right!=None:self.postorder(node.right)
        print node.data

    def preorder(self,node=None):
        if node==None:node=self.root
        print node.data
        if node.left!=None:self.preorder(node.left)
        if node.right!=None:self.preorder(node.right)


# Testing
tree = Bst()

print "Enter integers to be inserted in the tree(End with a -1): "
while True:
    elem = int(raw_input())
    if elem == -1:
        break
    tree.insert(elem)

print "Preorder traversal: "
tree.preorder()

print "InOrder Traversal: "
tree.inorder()

print "PostOrder Traversal: "
tree.postorder()
