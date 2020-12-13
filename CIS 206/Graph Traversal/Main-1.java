import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Scanner;

public class Main {

	private ArrayList<Node> graph = new ArrayList<>();
	Node starter;
	
	
	public Main() {
		//TODO put your Scanner stuff here.
		Scanner s = new Scanner(System.in);
		String beatriz = s.nextLine();
		String[] Kelly = beatriz.split(" ");
		for (var k : Kelly) {
			graph.add(new Node(k));
		}
		
		String lana = s.next();
		starter = findByName(lana);
		
		while(true) {
			String a = s.next();
			if(a.equals("***")) {
				break;
			}
			String b = s.next();
			Node n1 = findByName(a);
			Node n2 = findByName(b);
			n1.addNeighbor(n2);
			n2.addNeighbor(n1);
		}
		//print the all node neighbors
		for (var n : graph) {
			n.printing();
		}
		System.out.println("");
		//print the all graph travel
		System.out.println("Depth-First Search:");
		depthFirst(starter);
		System.out.println("");
		System.out.println("Breadth-First Search:");
		breadthFirst(starter);
	}
	public void depthFirst(Node a) {
		//TODO follow the book's pseudocode
		//set the a visited as true 
		a.visited = true;
		//print the node a name of depth first
		System.out.print(a.name+" ");
		for (Node n : a.neighbors) {
			if(n.visited ==false) {
				depthFirst(n);
			}
		}
		
	}
	
	public void breadthFirst(Node a) {
		Queue<Node> q = new ArrayDeque();
		//TODO follow the book's pseudocode
		//clear the quere and print out the node a and n
		q.clear();
		a.visited = false;
		System.out.print(a.name+" ");
		q.offer(a);
		while(!q.isEmpty()) {
			for(Node n : q.peek().neighbors ) {
				if(n.visited == true) {
					n.visited = false;
					System.out.print(n.name+" ");
					q.offer(n);
				}
			}
			q.poll();
		}
	}
	
	public Node findByName(String tiana) {
		//TODO follow whiteboard pseudocode
		//for each node in graph, it will return n if the string is node n
		for(Node n : graph) {
			if(tiana.equals(n.name)) {
				return n;
			}
		}return null;
	}

	public static void main(String[] args) {
		new Main();
	}


}
