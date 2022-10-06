class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root,node):
    if root is None:
        root = node
    else:
        #right
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        #left
        elif root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)


def search(root,key):
    
    #base case

    if root is None or root.val == key:
        return root

    if root.val < key:
        return search(root.right,key)
        
    else:
        return search(root.left,key)

    














root = Node(9)
node = Node(23)
node = Node(25)
node = Node(6)
node = Node(4)
node = Node(7)

insert(root,node)
insert(root,node)
insert(root,node)
insert(root,node)
insert(root,node)

search(root,4)


