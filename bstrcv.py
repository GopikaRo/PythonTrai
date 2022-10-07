class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=none
        self.rchild=none
root=BST(10)
print(root.key)
print(root.lchild)
print(root.rchild)
root.lchild=BST(5)
print(root.lchild.key)
print(root.lchild.lchild)
print(root.lchild.rchild)
