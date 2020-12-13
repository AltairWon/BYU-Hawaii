import javax.swing.*;
import java.awt.Graphics;

public class Jan29 extends JPanel {
	
	int age;
	ImageIcon picture1;
	ImageIcon picture2;
	ImageIcon picture3;
	ImageIcon picture4;
	ImageIcon picture5;
	ImageIcon picture6;
	ImageIcon picture7;
	ImageIcon picture8;
	ImageIcon picture9;
	int x;
	
	public Jan29() {
		//Your custom initialization code here
		String[] gender = {"Male", "Female"};
		x = JOptionPane.showOptionDialog(null, "What is your gender?", 
			"Click a button",JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, gender, gender[0]);
			String rex = JOptionPane.showInputDialog("What is your age?");
			age = Integer.parseInt(rex);
			picture1 = new ImageIcon("rockchapel.jpg");
			picture2 = new ImageIcon("beehive.gif");
			picture3 = new ImageIcon("laurel.gif");
			picture4 = new ImageIcon("miamaid.gif");
			picture5 = new ImageIcon("RS.jpg");			
			picture6 = new ImageIcon("deacon.jpg");
			picture7 = new ImageIcon("teacher.jpg");
			picture8 = new ImageIcon("priest.jpg");
			picture9 = new ImageIcon("elders.jpg");	
	}
	
	public void paintComponent(Graphics g) { 
		if (x == 1) {	//Female Picture	
			if (age >= 0 && age < 12) {
			g.drawString("You go to Primary!",90, 60);
			picture1.paintIcon(null, g, 80, 70);
			} 	if (age >= 12 && age <= 13) {
			g.drawString("You belong to the Beehive class.",50, 20);
			picture2.paintIcon(null, g, 35, 30);
			}	if (age > 13 && age <= 15) {
			g.drawString("You belong to the Miamaid class",50, 20);
			picture3.paintIcon(null, g, 30, 30);
			}	if (age > 15 && age <= 17) {
			g.drawString("You belong to the Laurel class.",55, 20);
			picture4.paintIcon(null, g, 25, 30);
			}	if (age > 17 && age <= 119) {
			g.drawString("You are a member of the Relief Society.",10, 10);
			picture5.paintIcon(null, g, 10, 10); 
			}	if (age < 0 || age >=120)	{
			g.drawString("Are you sure you typed that correctly?",10,10);
			}
		}
		if (x == 0){ //Male Picture
			if (age >= 0 && age < 12) {
			g.drawString("You go to Primary!",90, 60);
			picture1.paintIcon(null, g, 80, 70);
			} 	if (age >= 12 && age <= 13) {
			g.drawString("You belong to the Deacons quorum.",50, 20);
			picture6.paintIcon(null, g, 35, 30);
			}	if (age > 13 && age <= 15) {
			g.drawString("You belong to the Teachers quorum",50, 20);
			picture7.paintIcon(null, g, 30, 30);
			}	if (age > 15 && age <= 17) {
			g.drawString("You belong to the Priests quorum.",55, 20);
			picture8.paintIcon(null, g, 25, 30);
			}	if (age > 17 && age <= 119) {
			g.drawString("You belong to the Elders quorum.",10, 10);
			picture9.paintIcon(null, g, 10, 10); 
			}	if (age < 0 || age >=120)	{
			g.drawString("Are you sure you typed that correctly?",10,10);
			}		
		} 
	}

	public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(300,300);
		window.setContentPane(new Jan29());
		window.setVisible(true);
	}
	
}