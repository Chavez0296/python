'''
● isEmpty()
    ○ I/P: none
    ○ O/P: boolean value
● insertHead() - adds an element to the head
    ○ I/P: element to add
    ○ O/P: none
● removeHead() - removes and returns the current head element, and updates the head
to the new head
    ○ I/P: none
    ○ O/P: head element
● insertTail() - adds an element to the tail of the list
    ○ I/P: element to add
    ○ O/P: none
● removeTail() - removes and returns the current tail element, and updates the tail to the
new tail
    ○ I/P: none
    ○ O/P: tail element
● insertAtPos() - inserts element at specified position and updates the next and previous
elements of its neighboring elements
    ○ I/P: element to add, position
    ○ O/P: none
● traverse() - iterate through the entire list and print out each value
    ○ I/P: none
    ○ O/P: none
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self):
        if self.head is None: #if there is no head, then the list empty
            return True 
        return False
    
    def insertHead(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode # if the list is empty then the first node is the head
            return
        else:
            newNode.next = self.head #new node points to old head node
            self.head = newNode # head is now the newNode
    
    def removeHead(self):
        if self.head is None:
            return
        
        self.head = self.head.next #if the list isn't empty then head will be set to the next node, which will result in the old head being removed
    
    def insertTail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode #if the list is empty then the head is the tail
            return
        
        currNode = self.head
        while(currNode.next):
            currNode = currNode.next # if the list isn't empty then we traverse the linkedlist until we hit the end
        
        currNode.next = newNode # set the last node.next to the newNode

    def removeTail(self):
        if self.isEmpty() == True:
            return 

        currNode = self.head
        while(currNode != None and currNode.next.next != None): # while the node isn't None and the next next node isn't none
            currNode = currNode.next # currNode is one node before the last so we can set next to None
        
        currNode.next = None
    
    def insertAtPos(self, data, idx):
        if idx == 0:
            self.insertHead(data) #idx 0 is the head
        
        count = 0
        currNode = self.head
        while(currNode != None and count+1 != idx):
            count = count+1   #increment count
            currNode = currNode.next #go to the next node
        
        if currNode != None:  
            newNode = Node(data) 
            newNode.next = currNode.next #newNode next ptr = to currNode.next
            currNode.next = newNode #currNode next ptr = to newNode itself 
        
        else:
            print("Error: Index not found")
        
    def traverse(self):
        currNode = self.head

        while(currNode):
            print(currNode.data)
            currNode = currNode.next

llist = LinkedList()

llist.insertHead('A')
llist.insertTail('B')
print(llist.isEmpty())
llist.traverse()
print("=-=-=-=-=-=-=-=-==-=-=-=")
llist.insertAtPos('C', 1)
llist.traverse()
print("=-=-=-=-=-=-=-=-==-=-=-=")
llist.removeHead()
llist.removeTail()
llist.traverse()
print("=-=-=-=-=-=-=-=-==-=-=-=")         
llist.removeHead()
print(llist.isEmpty())