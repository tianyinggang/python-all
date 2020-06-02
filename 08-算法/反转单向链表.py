'''


'''
class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def reverseLinked(header):
    if not header or not header.next:
        return header

    pre = None  # 前一个节点
    curNode = header
    while curNode:
        tmp = curNode.next   # 临时保存下一个节点
        curNode.next = pre   # 将前一个节点赋给当前节点的next
        pre = curNode
        curNode = tmp
    return pre

header = LinkedNode(0)
node1 = LinkedNode(1)
header.next = node1
node2 = LinkedNode(2)
node1.next = node2
node3 = LinkedNode(3)
node2.next = node3

def printLinked(header):
    p = header
    while p:
        print(p.val, end=' ')
        p = p.next
    print()
printLinked(header)
header = reverseLinked(header)
printLinked(header)

