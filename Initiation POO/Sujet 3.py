class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)
myLinkedList.head = myNode1
myNode1.next = myNode2
myNode2.next = myNode3
myNode3.next = myNode4
print("The elements in the linked list are:")
print(myLinkedList.head.data, end=" ")
print(myLinkedList.head.next.data, end=" ")
print(myLinkedList.head.next.next.data, end=" ")
print(myLinkedList.head.next.next.next.data)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
myNode = Node(10)
print("The data in the node is:", myNode.data)
print("The next attribute in the node is:", myNode.next)