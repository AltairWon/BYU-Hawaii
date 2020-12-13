import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

public class Node implements Comparable<Node> {

	String name;
	List<Node> neighbors;
	boolean visited;
	
	public Node(String n) {
		name = n;
		neighbors = new ArrayList<>();
		visited = false;
	}
	
	public void addNeighbor(Node n) {
		neighbors.add(n);
		Collections.sort(neighbors);
	}
	
	@Override
	public int compareTo(Node other) {
		//the ordering of edges is the same as
		//alphabetical order
		return this.name.compareTo(other.name);
	}
	
	/**
	 * print all the node neighbors in input file
	 */
	public void printing() {
		System.out.print(name + ": ");
		for (var n : neighbors) {
			System.out.print(n.name + " ");
		}
		System.out.println("");
	}
}
