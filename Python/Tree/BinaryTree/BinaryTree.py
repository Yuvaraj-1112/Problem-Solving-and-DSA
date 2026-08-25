class BinaryTree:

    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self,data):
        self.root = self.Node(data)

    def InsertLeft(self,node,data):
        node.left = self.Node(data)

    def InsertRight(self,node,data):
        node.right = self.Node(data)

    def PreOrder(self,root):
        if root is None: 
            return
        
        print(root.data, end=" ")
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def InOrder(self,root):
        if root is None:
            return
        
        self.InOrder(root.left)
        print(root.data, end=" ")
        self.InOrder(root.right)

    def PostOrder(self,root):
        if root is None:
            return
        
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data, end=" ")

bt = BinaryTree(1)
bt.InsertLeft(bt.root,2)
bt.InsertRight(bt.root,3)
bt.InsertLeft(bt.root.right,7)
bt.InsertRight(bt.root.right,8)

bt.PreOrder(bt.root)
print()
bt.InOrder(bt.root)
print()
bt.PostOrder(bt.root)

