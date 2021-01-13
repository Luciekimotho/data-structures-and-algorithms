class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

    
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)

def printWithQueue(root):
    if root is None:
        return
    
    queue = []
    queue.append(root)

    while (len(queue) > 0):
        
        # for i in range(len(queue)):
        #     print(queue[i].val, end=" ")

        print(queue[0].val, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
print(" Newline")
def printInOrder(root):
    if root is None:
        return
    else:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)

root = Node(0)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.right.left = Node(3)
root.right.right = Node(9)
print(" Level order")
printWithQueue(root)

print(" In order")
print(" In order")
printInOrder(root)

