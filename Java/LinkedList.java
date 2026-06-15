class Node {
    int data;
    Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class LinkedList{
    Node head = null;
    
    void InsertBegging(int data){
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    void InsertLast(int data){
        if(head == null){
            InsertBegging(data);
        }
        Node newNode = new Node(data);
        Node temp = head;
        while(temp.next != null){
            temp = temp.next;
        }
        temp.next = newNode;
    }

    void InsertIndex(int index, int data){
        if(index < 0){
            System.out.println("Invalid Syntax");
            return;
        }

        Node temp = head;
        for(int i =0; i<index-1; i++){
            temp = temp.next;
        }
        Node newNode = new Node(data);
        newNode.next = temp.next;
        temp.next = newNode;
    }

    void Delete(int data){
       Node temp = head;

       if(temp.data == data){
        temp = temp.next;
        return;
       }

       while(temp.next != null && temp.next.data != data){
        temp = temp.next;
       }

       if(temp.next == null){
        System.out.println("Invalid Index");
        return;
       }
       
       temp.next = temp.next.next;

    }

    void DeleteIndex(int index){
        Node temp = head;
        if(index == 0){
            System.out.println("Invalid Index");
            return;
        }
        if(index == 0){
            temp = temp.next;
            return;
        }

        for(int i = 0; i<index-1; i++){
            temp = temp.next;
        }
        temp.next = temp.next.next;
    }

    void Search(int data){
        Node temp = head;
        int count = 0;
        while(temp != null){
            if(temp.data == data){
                System.out.println("Data found at Index " + count);
                return;
            }
            temp = temp.next;
            count++;
        }
        System.out.println("Data not found");
    }

    void display(){
        Node temp = head;
        while(temp != null){
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("Null");
    }

    public static void main(String args[]){
        LinkedList list = new LinkedList();
        
        list.InsertBegging(1);
        list.InsertBegging(2);
        list.InsertBegging(3);
        list.InsertLast(4);
        list.InsertIndex(2, 5);
        list.Delete(5);
        list.DeleteIndex(1);
        list.Search(5);

        list.display();
    }
}