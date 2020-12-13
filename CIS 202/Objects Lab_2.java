import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class PyramidFun extends JPanel {
	
	Pyramid pyramid1;
	Pyramid pyramid2;
	
	public PyramidFun() {
		pyramid1 = new Pyramid();
		pyramid2 = new Pyramid(120, 20);
	}
		
	@Override
	public void paintComponent(Graphics g) {
		int w = getWidth();
		int h = getHeight();
		
		//draw a green background and sun
		/*g.setColor(Color.GREEN);
		g.fillRect(0,0,w,h);*/
		g.setColor(new Color(0,255,255)); //sky
		g.fillRect(0,0,w,h);
		
		g.setColor(new Color(0,255,125)); //ground
		g.fillRect(0,200,w,h);
		
		g.setColor(new Color(0,255,0)); //Vegetation
		g.fillRect(0,100,w,100);
		g.fillOval(-25,75,50,50);
		g.fillOval(75,50,50,80);
		g.fillOval(125,80,80,50);
		g.fillOval(205,75,95,60);
		
		g.setColor(Color.YELLOW); //Sun
		g.fillOval(20,10,50,50);
	
		pyramid1.draw(g);
		pyramid2.draw(g);
	}

	public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(350,350);
		window.setContentPane(new PyramidFun());
		window.setVisible(true);
	}
}
