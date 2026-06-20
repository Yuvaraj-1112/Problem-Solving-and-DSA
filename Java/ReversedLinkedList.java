import  java.util.Scanner;

class Node{
    int data;
    Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class LinkedList{
    Node head = null;

    void inslast(int data){
       Node newNode = new Node(data);

       if(head == null){
        head = newNode;
        return;
       }

       Node temp = head;

       while(temp.next != null){
        temp = temp.next;
       }
       temp.next = newNode;
    }

    void display(){
        Node temp = head;

        while(temp != null){
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("Null");
        System.out.println();
    }

    void revlinkedlist(int data){

        Node temp = head;

        Node Prev = null;
        Node Current = head;
        Node Next = null;

        while(Current != null){
            Next = Current.next;
            Current.next = Prev;
            Prev  = Current;
            Current = Next;
        }

        head = Prev;

    }
}

class ReversedLinkedList{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        LinkedList list = new LinkedList();

        for(int i=0; i<n; i++ ){
            int data = sc.nextInt();
            list.inslast(data);
        }

        list.display(); 

          for(int i=0; i<n; i++ ){
            int data = sc.nextInt();
            list.revlinkedlist(data);
        }

        list.display();
    }
}