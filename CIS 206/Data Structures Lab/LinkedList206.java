
public class LinkedList206<E> {

	Node206<E> head;
	
	public LinkedList206() {
		head = null;
	}
	
	public void add(E k) {
		Node206<E> n = new Node206<E>(k);
		if (head == null) {
			head = n;
		} else {
			//add the new node to the
			//end of the list.
			Node206<E> tmp = head;
			while (tmp.next != null) {
				tmp = tmp.next;
			}
			tmp.next = n;
		}
	}
	
	public void printAll() {
		Node206<E> tmp = head;
		while (tmp != null) {
			System.out.println(tmp.data);
			tmp = tmp.next;
		}
	}
	
	public E get(int index) {
		Node206<E> tmp = head;
		for (int i=0; i<index; i++) {
			tmp = tmp.next;
		}
		return tmp.data;		
	}
	
	public E removeAt(int index) {
		E result;
		Node206<E> tmp = head;
		if (index == 0) {
			result = head.data;
			head = head.next;
		} else {
			for (int i=0; i<index-1; i++) {
				tmp = tmp.next;
			}
			result = tmp.next.data;
			tmp.next = tmp.next.next;
		}
		return result;
	}
	
	public void insertAt(int index, E newData) {
		Node206<E> n = new Node206<E>(newData);
		Node206<E> tmp = head;
		if (index == 0) {
			n.next = head;
			head = n;
		} else {
			for (int i=0; i<index-1; i++) {
				tmp = tmp.next;
			}
			//make the new node point to the rest of the list
			n.next = tmp.next;
			
			//make the node before it, point to the new node
			tmp.next = n;
		}
	}
	//TODO make the length of the node and temp for removing stack and queue
	public int length() {
		Node206 <E>temp=head;
		int count = 0;
		while(temp != null) {
			count++;
			temp = temp.next;
		}return count;
	}
	
	//TODO clear all stacks and queue if the head is 0
	public void clear() {
		head=null;
		
	}
	//TODO checking the stack and queue if the stack or queue are empty
	public boolean emptyCheck() {
		if(head==null) {
			return true;
		}else {
			return false;
		}
		
	}
}