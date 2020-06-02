'''
中序遍历



'''

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class KNode:
    def kthNode(self,pRoot,k):
        global result
        result = []
        middle = self.midorder(pRoot)
        if k <= 0 or len(middle) < k:
            return None
        else:
            return middle[k - 1]

    def midorder(self,pRoot):
        if not pRoot:
            return []
        self.midorder(pRoot.left)
        result.append(pRoot)
        self.midorder(pRoot.right)
        return result

root = TreeNode(10)
left = TreeNode(6)
right = TreeNode(15)
root.left = left
root.right = right

left1 = TreeNode(11)
right1 = TreeNode(20)

right.left = left1
right.right = right1

print(KNode().kthNode(root,3).val)