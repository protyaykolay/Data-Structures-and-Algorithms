class Node:
    def __init__(self,value=None):
        self.data = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = None
        
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
            
        t = self.head
        while(t.next != None):
            t = t.next
        
        t.next = temp
        temp.prev = t
        
    def insertAtBegin(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        
    def insertAtMiddle(self,value,x):
        t = self.head
        
        while(t.next != None):
            if(t.data == x):
                break
            t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t
        
    def printdLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data, end=" <--> ")
            t1 = t1.next
        print(t1.data)
        
    def deletetionDLL(self,value):
        if(self.head == None):
            print("Linked List is empty")
            return
        
        t = self.head
        if(t.data == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next
        if(t.data == value):
            t.prev.next = None
            
        
obj = DoublyLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBegin(5)
obj.insertAtMiddle(50,20)
obj.deletetionDLL(5)
obj.deletetionDLL(50)
obj.deletetionDLL(40)
obj.printdLL()