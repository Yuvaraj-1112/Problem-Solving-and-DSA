import java.util.Scanner;

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

    void InsBeg(int data){
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    void InsLast(int data){

        Node newNode = new Node(data);
        if (head == null){
            head = newNode;
            return;
        }

        Node temp = head;
       while(temp.next != null){
        temp = temp.next;
       }
       temp.next = newNode;
    }

    void InsIndex(int index, int data){
        Node newNode = new Node(data);
        if(index < 0){
            System.out.println("Invalid Index");
        }

        if(index == 0){
        newNode.next = head;
        head = newNode;
        return;
        }

        Node temp = head;
        for(int i=0; i < index-1; i++){
            temp = temp.next;
        }
        newNode.next = temp.next;
        temp.next = newNode;
    }

    void Del(int data){
        Node temp = head;

        if(temp.data == data){
            temp = temp.next;
        }
        while(temp.next != null && temp.next.data != data){
            temp = temp.next;
        }
        if(temp.next == null){
            System.out.println("Data not found");
            return;
        }
        temp.next = temp.next.next;
    }

    void DelIndex(int index){
        Node temp = head;

        if(index < 0){
            System.out.println("Invalid Index");
        }

        if(index == 0){
            temp = temp.next;
        }

        for(int i=0; i <index-1; i++){
            temp = temp.next;
        }
        temp.next = temp.next.next;
    }

    void search(int data){
        Node temp = head;
        int count = 0;
        while(temp != null){
            if(temp.data == data){
                System.out.println("Value in index : "+count);
                return;
            }
            count++;
            temp = temp.next;
        }
        System.out.println("Data not found");
    }

    void display(){
        Node temp = head;
        while(temp != null){
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.print("NULL");
    }
}


public class LinkedListUpdated {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        LinkedList list = new LinkedList();

        System.out.println("Enter the number of nodes:");
        int n = sc.nextInt();

        System.out.println("Enter Nodes:");
        for(int i=0; i<n; i++){
            int data = sc.nextInt();
            list.InsLast(data);
        }

        System.out.println("Enter the index:");
        int index = sc.nextInt();
        
        System.out.println("Enter the indexing Data:");
        int indexdata = sc.nextInt();
        list.InsIndex(index, indexdata);

        System.out.println("Enter the Deleting Data:");
        int deldata = sc.nextInt();
        list.Del(deldata);

        System.out.println("Enter the Deleting Index:");
        int delindex = sc.nextInt();
        list.DelIndex(delindex);

        System.out.println("Enter the Searching Data:");
        int srdata = sc.nextInt();
        list.search(srdata);
  
        list.display();
        sc.close();
    }
}
