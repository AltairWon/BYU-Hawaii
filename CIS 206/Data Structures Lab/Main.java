import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		LinkedList206<String> lnl = new LinkedList206<>();
		Scanner s = new Scanner(System.in);
		while(true) {
			String line = s.nextLine();
			String[] newLine = line.split(" ");
			//TODO show the stack if the stack "PUSH"
			if(newLine.length==2) {
				lnl.add(newLine[1]);
			}
			//TODO removes the stacks from the top of the stacks for "POP"
			if(line.equals("POP")) {
				//TODO for checking the empty stack
				if(lnl.emptyCheck()==true) {
					System.out.println("Empty");
					
				}else {
				String v=lnl.removeAt(lnl.length()-1);
				System.out.println(v);
				}
			}
			//TODO print all current stack contents for "PRINT"
			if(line.equals("PRINT")) {
				lnl.printAll();
			}
			//TODO clear the stacks the stack for "CLEAR"
			if(line.equals("CLEAR")) {
				lnl.clear();
			}
			//TODO ends with a single line of ***
			if(line.equals("***")) {
				break;
			}
		}	
	}
}
