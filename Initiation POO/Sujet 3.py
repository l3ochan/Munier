class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def printNode(self):
        print(self.data, end=" ")
        if self.next is not None:
            self.next.printNode()
    
    def printNodeRev(self):
        print(self.data, end=" ")
        if self.prev is not None:
            self.prev.printNodeRev()

    def printCount(self):
        print(self.data, end=" ")
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printListRec(self):
        if self.head is not None:
            self.head.printNode()
    
    def printListRecRev(self):
        # Trouver le dernier node
        current = self.head
        if current is not None:
            while current.next is not None:
                current = current.next
            # Imprimer en ordre inverse
            current.printNodeRev()
    def countNodes(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def printCount(self):
        count = self.countNodes()
        print(f"There are {count} elements in the list.")
        
    def addInTail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    def addSorted(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        if new_node.data < current.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
            new_node.next = current.next
        if current.next is not None:
            current.next.prev = new_node  # Mettre à jour le prev du nœud suivant
            current.next = new_node  # Le suivant de current devient new_node
            new_node.prev = current
    def reverseList(self):
        reversedList = LinkedList()
        current = self.head
        # Parcourir la liste originale
        while current is not None:
            # Ajouter chaque élément à la tête de la nouvelle liste
            new_node = Node(current.data)  # Créer un nouveau nœud avec la même donnée
            new_node.next = reversedList.head
            if reversedList.head is not None:
                reversedList.head.prev = new_node
            reversedList.head = new_node
            current = current.next  # Passer au nœud suivant
        return reversedList
        
print()
myLinkedList = LinkedList()
myNode1 = Node(10)
myNode2 = Node(20)
myNode3 = Node(30)
myNode4 = Node(40)
myLinkedList.head = myNode1
myNode1.next = myNode2
myNode2.prev = myNode1
myNode2.next = myNode3
myNode3.prev = myNode2
myNode3.next = myNode4
myNode4.prev = myNode3
print("The elements in the linked list are:")
myLinkedList.printListRec()
print("\nThe elements in the linked list in reverse order are:")
myLinkedList.printListRecRev()
myLinkedList.printCount()