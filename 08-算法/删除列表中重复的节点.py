class LinkedNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def deleteDuplication(pHead):
    nodeValues = {}
    newHead = LinkedNode(pHead.val)
    nodeValues[pHead.val] = pHead.val

    curNode = newHead
    while pHead.next:
        pHead = pHead.next
        if nodeValues.get(pHead.val) == None:
            curNode.next = LinkedNode(pHead.val)
            curNode = curNode.next
            nodeValues[pHead.val] = pHead.val
    return newHead
header = LinkedNode(5)
node1 = LinkedNode(5)
header.next = node1
node2 = LinkedNode(10)
node1.next = node2
node3 = LinkedNode(4)
node2.next = node3

def printLinked(header):
    p = header
    while p:
        print(p.val)
        p = p.next
header = deleteDuplication(header)
printLinked(header)