import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;
import java.io.*;
import java.util.*;

public class Feb12 extends JPanel {
	int i;
	int j;
	int [][] altair = new int [200][200];
	
	public Feb12() {
		for (i = 0; i<200; i++){
			for (j=0; j<200; j++){
				altair[i][j] = 0;
				
				
			}
		}
		var filename = "stars2.txt"; // seting the file
		var f = new File(filename);
		try {
			var s = new Scanner(f); //read the file
			while (s.hasNext() == true) {
				int x = s.nextInt();
				int y = s.nextInt();
				altair[x][y] = 1;
				altair[x-1][y-1] = 1;
				altair[x-2][y-2] = 1;
				altair[x-3][y-3] = 1;
				altair[x-1][y+1] = 1;
				altair[x-2][y+2] = 1;
				altair[x-3][y+3] = 1;
				altair[x+1][y-1] = 1;
				altair[x+2][y-2] = 1;
				altair[x+3][y-3] = 1;
				altair[x+1][y+1] = 1;
				altair[x+2][y+2] = 1;
				altair[x+3][y+3] = 1;
			}
			s.close();
		} catch (FileNotFoundException e) {
			System.out.println("Yo! File not found!!!!");
		}
	}
	
	@Override
	public void paintComponent(Graphics g) {
		//g.setColor(Color.BLACK);  //set the black background
		//g.fillRect(0,0,getWidth(),getHeight());
		for (int a=0; a<200; a++) 
			for (int b=0; b<200; b++)
				if (altair[a][b] == 0) {
					//g.setColor(Color.WHITE); //set the white color
					//g.fillRect(a,b,1,1);
					g.setColor(Color.BLACK); //set the black color //method 2
					g.fillRect(a-1,b-1,getWidth(),getHeight());
				}
				else {
					g.setColor(Color.WHITE); //set the white color
					g.fillRect(a-1,b-1,a,b);
				}
	}

	public static void main(String[] args) {
		JFrame window = new JFrame();
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setSize(250,250);
		window.setContentPane(new Feb12());
		window.setVisible(true);
	}
}