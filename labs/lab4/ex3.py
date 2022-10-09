from ex2 import Queue
class BinaryTree:
    def __init__(self,data=None,left=None,right=None):  # 如果创建节点对象时left或right参数为空，则默认该节点没有左或右子树
        self.data=data
        self.left=left
        self.right=right
    def preorder(self):  # 前序遍历
        print(self.data,end=' ')
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
    def midorder(self):  # 中序遍历
        if self.left != None:
            self.left.midorder()
        print(self.data,end=' ')
        if self.right != None:
            self.right.midorder()
    def postorder(self):  # 后序遍历
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        print(self.data,end=' ')
    def height(self):
        if self.data is None:  # 空的树高度为0, 只有root节点的树高度为1
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())
    def levelorder(self):
        q = Queue()
        q.enqueue(self)
        while q.empty() == False:
            cur = q.dequeue()
            print(cur.data)
            if cur.left != None:
                q.enqueue(cur.left)
            if cur.right != None:
                q.enqueue(cur.right)
        pass

layer3_2 = BinaryTree(2,BinaryTree(7),BinaryTree(4))
layer2_5 = BinaryTree(5,BinaryTree(6),layer3_2)
layer2_1 = BinaryTree(1,BinaryTree(0),BinaryTree(8))
layer1_3 = BinaryTree(3,layer2_5,layer2_1)
layer1_3.levelorder()