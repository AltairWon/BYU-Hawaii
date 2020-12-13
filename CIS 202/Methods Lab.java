import javax.swing.JFrame;
import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.util.*;

public class Feb20 extends JPanel {
	ArrayList<String> instructions = new ArrayList<String>();
	
	public void changeColor(int red, int green, int blue, Graphics g) {
		g.setColor(new Color(red,green,blue)); //set the color
	} 
	public void drawTriangle(int x1, int y1, int x2, int y2, int x3, int y3, Graphics g ) {
		g.drawLine(x1,y1,x2,y2);
		g.drawLine(x2,y2,x3,y3); //draw the line that make the triangle
		g.drawLine(x3,y3,x1,y1);
	} 
	public void drawCircle(int xc, int yc, int r, Graphics g) {
		g.drawOval(xc-r,yc-r,r*2,r*2); 
	}
	
	
	public Feb20() {
		String rex = JOptionPane.showInputDialog("What is the filename?");
		File f = new File(rex); // rex equals the input string name.
		try {
			Scanner s = new Scanner(f); //read the text file
			while (s.hasNext() == true) {
				String line = s.nextLine();
				//String[] rex = line.split(",");
				instructions.add(line); //store the text file
			}
			s.close();
		} catch(FileNotFoundException e) { //catch if the file is not right
			System.out.println("Yo! File not found!!!!");
		}
	}
	
	public void parseCommand(String command, Graphics g)	{
	String[] don = command.split(" ");
	if(don[0].equals("COLOR")) { //set up the color
		int red = Integer.parseInt(don[1]);
		int green = Integer.parseInt(don[2]);
		int blue = Integer.parseInt(don[3]);
		changeColor(red,green,blue,g);
	}
	if(don[0].equals("TRIANGLE")) { //set up the triangle
		int x1 = Integer.parseInt(don[1]);
		int y1 = Integer.parseInt(don[2]);
		int x2 = Integer.parseInt(don[3]);
		int y2 = Integer.parseInt(don[4]);
		int x3 = Integer.parseInt(don[5]);
		int y3 = Integer.parseInt(don[6]);
		drawTriangle(x1,y1,x2,y2,x3,y3,g);
	}
	if(don[0].equals("CIRCLE")) { //set up the circle
		int xc = Integer.parseInt(don[1]);
		int yc = Integer.parseInt(don[2]);
		int r = Integer.parseInt(don[3]);
		drawCircle(xc,yc,r,g);
	}
	}
	
	
	@Override
	public void paintComponent(Graphics g) {
		for (String rex : instructions) { //read the array and parseCommand
		parseCommand(rex,g);
		//bring parseCommand
		}
	}

	public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(300,300);
		window.setContentPane(new Feb20());
		window.setVisible(true);
	}
}