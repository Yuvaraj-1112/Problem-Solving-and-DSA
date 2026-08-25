class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            nexxt = current.next
            current.next = prev
            prev = current 
            current = nexxt

        self.head =  prev


    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

ll = LinkedList()


a = list(map(int,input().split()))

for num in a:
    ll.insert_last(num)

ll.display()  

ll.reverse()

ll.display()