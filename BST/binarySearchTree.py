class TreeNode :
    def __init__(self, newItem, left, right) :
        self.item = newItem
        self.left = left
        self.right = right
        self.visited = False
    
class BinarySearchTree :
    def __init__(self) :
        self.__root = None

    def search(self, x) -> TreeNode :
        return __searchItem(self.__root, x)
    
    def __searchItem(self, tNode:TreeNode, x) -> TreeNode :
        if (tNode == None) :
            return None
        elif (x == tNode.item) :
            return tNode
        elif (x < tNode.item) :
            return self.__searchItem(tNode.left, x)
        else :
            return self.__searchItem(tNode.right, x)
        
    def insert(self, newItem) :
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode :
        if (tNode == None) :
            tNode = TreeNode(newItem, None, None)
        elif (newItem < tNode.item) :
            tNode.left = self.__insertItem(tNode.left, newItem)
        else :
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode
    
    def delete(self, x) :
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode :
        if (tNode == None) :
            return None
        elif (x == tNode.item) : 
            tNode = self.__deleteNode(tNode)
        elif (x < tNode.item) :
            tNode.left = self.__deleteItem(tNode.left, x)
        else :
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode
    
    def __deleteNode(self, tNode:TreeNode) -> TreeNode :
        if tNode.left == None and tNode.right == None :
            return None
        elif tNode.left == None :
            return tNode.right
        elif tNode.right == None :
            return tNode.left
        else :
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode
        
    def __deleteMinItem(self, tNode:TreeNode) -> tuple :
        if tNode.left == None :
            return (tNode.item, tNode.right)
        else :
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            return (rtnItem, tNode)
        
    def isEmpty(self) -> bool :
        return self.__root == self.NIL
    
    def clear(self) :
        self.__root = self.NIL

    def getRoot(self) :
        return self.__root

    def preOrder(self, r:TreeNode) :
        if r != None :
            r.visited = True
            print(r.item, end = ' ')
            self.preOrder(r.left)
            self.preOrder(r.right)

    def inOrder(self, r:TreeNode) :
        if r != None :
            self.inOrder(r.left)
            r.visited = True
            print(r.item, end = ' ')
            self.inOrder(r.right)

    def postOrder(self, r:TreeNode) :
        if r != None :
            self.postOrder(r.left)
            self.postOrder(r.right)
            r.visited = True    
            print(r.item, end = ' ')

    def lca(self, item1, item2) :
        Node1 = self.search(item1)
        Node2 = self.search(item2)

        # Keep coding
        
