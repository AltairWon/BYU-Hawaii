import javax.swing.JPanel;
import javax.swing.JFrame;
import java.awt.Graphics;

public class Knockknock extends JPanel { //set the new file name and use JPanel

	public void paintComponent(Graphics g) {
		g.drawString("A: Knock Knock!", 10,20); // Make simple sentences with setting x range and y range
		g.drawString("B: Who's there?", 10,40);
		g.drawString("A: Kim.", 10,60);
		g.drawString("B: Kim who?", 10,80); 
		g.drawString("A: KimChi!", 10,100);
	}

	public static void main(String[] args) {
		var window = new JFrame();
		window.setSize(200,200); //Set the size of Java frame
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Exit all process of Java
		window.setContentPane(new Knockknock()); //Set new class on Pane
		window.setVisible(true);//Make it visiable
	}

}
