class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def findPath(root, n):
    if not root:
        return []
    result = []
    def findPath2(root, path,currentNum):
        currentNum += root.val
        path.append(root)
        # 判断root是否为叶子节点
        flag = root.left == None and root.right == None

        if currentNum == n and flag:
            onepath = []
            for node in path:
                onepath.append(node.val)
            result.append(onepath)
        if currentNum < n:
            if root.left:
                findPath2(root.left,path,currentNum)
            if root.right:
                findPath2(root.right,path,currentNum)
        path.pop()
    findPath2(root,[],0)
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

left2 = TreeNode(9)
left1.left = left2

'''
            10
         6      15   
             11   20
           9   
'''

print(findPath(root,16))
print(findPath(root,45))