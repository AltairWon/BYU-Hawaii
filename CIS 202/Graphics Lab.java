import javax.swing.*;
import java.awt.*;

public class HJPyramid extends JPanel {
	
	public HJPyramid() {
	}
	@Override
	public void paintComponent(Graphics g) {
		
		var dy = 0; //Change int y so that it can make above.
		var w = getWidth();
		var h = getHeight();

		g.setColor(new Color(0,255,255)); //sky
		g.fillRect(0,0,w,h);
		
		g.setColor(new Color(0,255,125)); //ground
		g.fillRect(0,200,w,100);
		
		g.setColor(new Color(0,255,0)); //Vegetation
		g.fillRect(0,100,w,100);
		g.fillOval(-25,75,50,50);
		g.fillOval(75,50,50,80);
		g.fillOval(125,80,80,50);
		g.fillOval(205,75,95,60);
		
		g.setColor(Color.YELLOW); //Sun
		g.fillOval(20,10,50,50);
		
		g.setColor(new Color(134,134,134)); //Pyramid
		g.fillRect(110,130+dy,80,30);
		g.fillRect(100,160+dy,100,20);
		g.fillRect(90,180+dy,120,20);
		g.fillRect(80,200+dy,140,20);
		g.fillRect(70,220+dy,160,20);
		
		g.setColor(Color.WHITE); //Cloud
		g.fillOval(80,15,30,30);
		g.fillOval(100,15,30,30);
		g.fillOval(120,15,30,30);
		g.fillOval(150,50,30,30);
		g.fillOval(170,50,30,30);
		g.fillOval(190,50,30,30);
		g.fillOval(220,15,30,30);
		g.fillOval(240,15,30,30);
		g.fillOval(260,15,30,30);
		
		g.setColor(Color.BLACK); //Stair
		g.drawLine(110,230+dy,190,230+dy);
		g.drawLine(120,225+dy,180,225+dy);
		g.drawLine(130,220+dy,170,220+dy);
		g.drawString("HJ's Pyramid!",110,255);
		

	}

	public static void main(String[] args) {
		var window = new JFrame("Let us make Pyramid");
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(310,310);
		window.setContentPane(new HJPyramid());
		window.setVisible(true);
	}
}