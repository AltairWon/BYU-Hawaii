import javax.swing.*;
import java.awt.*;

public class Feb5 extends JPanel {
	int stripes;
	int rows;
	int columns;
	
	public Feb5() {
		String rex1 = JOptionPane.showInputDialog("How many stripes do you want?");
		stripes = Integer.parseInt(rex1);
		String rex2 = JOptionPane.showInputDialog("How many rows do you want?");
		rows = Integer.parseInt(rex2);
		String rex3 = JOptionPane.showInputDialog("How many columns do you want?");
		columns = Integer.parseInt(rex3);
	}

	@Override
	public void paintComponent(Graphics g) {
		var w = getWidth();
		var h = getHeight();
		var y1 = h/stripes; //first white stripes
		var y2 = h/stripes; //repeat white stripes
		var bh = 7*y2; //blue box's height
		var bw = w*2/5; //blue box's width
		var wh = bh/columns; //stars' columns
		var ww = bw/rows; //stars' rows
		
		//make red color first
		g.setColor(Color.RED);
		g.fillRect(0,0,w,h);
		
		//make white stripes
		g.setColor(Color.WHITE);
		g.fillRect(0,y1,w,y1);
		for (int i = 0; i < h; i++){
			g.fillRect(0,y1,w,y2);
			y1 += 2*y2;
		}
		
		//make blue box
		g.setColor(Color.BLUE);
		g.fillRect(0,0,bw,bh);
		//make white stars
		g.setColor(Color.WHITE);
		int x = 0;
		int y = 0;
		for (int i = 0; i <columns; i++){
			for (int j = 0; j <rows; j++) {
			g.fillOval(x,y,ww,wh);
			x += ww;
			}
			x = 0;
			y += wh;
		}
	}

	public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(600,450);
		window.setContentPane(new Feb5());
		window.setVisible(true);
	}
}