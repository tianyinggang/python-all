'''
二叉搜索树
二叉排序树
二叉查找树


前序遍历
中序遍历
后序遍历

根节点

后序
1 4 7 6 3 13 14 10 8

前序
8, 3,1,6,4,7,10,14,13


算法
1. 找到根节点 8
2. 遍历序列，找到第一个大于等于根节点的元素i，则i左侧为左子树，右侧为右子树
3. 判断i右侧的节点是否都比根节点的值大，如果有比根节点值大的节点，直接返回False
4. 否则用递归的方式继续处理i左侧和右侧的节点

'''

def verifyBST(sequence):
    if not sequence:
        return False
    root = sequence[-1]

    i = 0

    for node in sequence[i:-1]:
        if node > root:
            break
        i += 1
    for node in sequence[i:-1]:
        if node < root:
            return False
    left = True
    if i > 0:
        left = verifyBST(sequence[:i])
    right = True
    if i < len(sequence) - 2 and left:
        right = verifyBST(sequence[i + 1:])
    return left and right

print(verifyBST([1,4,7,6,3,13,14,10,8]))
print(verifyBST([8, 3,1,6,4,7,10,14,13]))
