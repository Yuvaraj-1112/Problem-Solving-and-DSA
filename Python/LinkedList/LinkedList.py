
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsertBegining(self,data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node

    def InsertEnd(self,data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
            return


        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_Node

    def InsertIndex(self, index, data):
        new_Node = Node(data)

        if index < 0:
            print("Invalid Syntax")
            return
        
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node
            return


        temp = self.head

        for i in range(index - 1):

            if temp is None:
                return
            
            temp = temp.next
        
        if temp is None:
            return
        
        new_Node.next = temp.next
        temp.next = new_Node

    def Delete(self,key):
        temp = self.head

        if key == temp:
            temp = temp.next

        while temp.next and temp.next.data != key:
            temp = temp.next

        if temp.next is None:
            print("Invalid Data")
            return
        
        if temp.next.data == key:
            temp.next = temp.next.next
            return
        
    def DeleteIndex(self,index):

        temp = self.head

        if index < 0:
            print("Invalid Syntax")

        if index == 0:
            temp = temp.next

        for i in range(index-1):
            temp = temp.next

        temp.next = temp.next.next

    def Search(self,data):
        temp = self.head
        count = 0


        while temp:
            if temp.data == data:
                print("Data found at index", count)
                return

            count += 1
            temp = temp.next

    

    def Display(self):
        temp = self.head

        while temp:
            print(temp.data,end = " -> ")
            temp = temp.next
        print("Null")

l1 = LinkedList()
l1.InsertEnd(5)
l1.InsertEnd(4)
l1.InsertEnd(3)
l1.InsertEnd(2)
l1.InsertEnd(1)

l1.InsertIndex(0,6)



l1.Display()
