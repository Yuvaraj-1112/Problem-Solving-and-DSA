class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node  

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def insert_index(self,index,data):
        new_node = Node(data)

        if index < 0:
            print("Index out of bound")

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        temp = self.head
        
        for _ in range(index-1):
            
            if temp is None:
                return
            
            temp = temp.next

        if temp is None:
            return
        
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
             temp.next.prev = new_node
        
        temp.next = new_node
        

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

dll = DoubleLinkedList()
a = list(map(int,input().split()))

for num in a:
    dll.insert_end(num)

dll.insert_index(0,6)

dll.display()
        
        
        