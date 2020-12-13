import java.util.Scanner;

public class Queues {

	public static void main(String[] args) {
		LinkedList206<String> lnl = new LinkedList206<>();
		Scanner s = new Scanner(System.in);
		while(true) {
			String line = s.nextLine();
			String[] newLine = line.split(" ");
			//TODO add "n" to the tail of the queue for "ENQUEUE"
			if(newLine.length==2) {
				lnl.add(newLine[1]);
			}
			if(line.equals("DEQUEUE")) {
				if(lnl.emptyCheck()==true) {
					System.out.println("Empty");					
				}else {
				//TODO in order to add the tail of the queue, I need to remove the queue from bottom 
				String v=lnl.removeAt(0);
				System.out.println(v);
				}            
			}
			//TODO print the current queue contents for "PRINT"
			if(line.equals("PRINT")) {
				lnl.printAll();
			}
			//TODO clear the current contents array for "CLEAR"
			if(line.equals("CLEAR")) {
				lnl.clear();
			}
			//TODO ends with the single line of ***
			if(line.equals("***")) {
				break;
			}
		}
	}
}
