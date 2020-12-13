import java.awt.Color;
import java.awt.Graphics;

public class Pyramid {

	//in general, most fields should be private
	private Color pyramidColor;
	private Color stairColor;
	private Vertex position;
	
	//constructors are almost always public
	public Pyramid() {
		pyramidColor = Color.YELLOW;
		stairColor = Color.BLACK;
		position = new Vertex();
	}
	
	public Pyramid(int x, int y) {
		position = new Vertex(x,y);
		pyramidColor = Color.RED;
		stairColor = Color.WHITE;
	}
	
	//set the pyramid color
	public void setStairColor(Color c) {
		pyramidColor = c;
	}
	
	//set the stair color
	public void setPyramidColor(Color c) {
		stairColor = c;
	}
	
	
	//in general, most methods should be public
	//draw pyramid
	public void draw(Graphics g) {
		g.setColor(pyramidColor);		
		g.fillRect(position.x+50,position.y+130,80,30); //Pyramid
		g.fillRect(position.x+40,position.y+160,100,20);
		g.fillRect(position.x+30,position.y+180,120,20);
		g.fillRect(position.x+20,position.y+200,140,20);
		g.fillRect(position.x+10,position.y+220,160,20);
		g.setColor(stairColor);		//Make Stair
		g.drawOval(position.x+65,position.y+135,50,30);
		g.drawLine(position.x+70,position.y+230,position.x+120,position.y+230);
		g.drawLine(position.x+80,position.y+225,position.x+110,position.y+225);
		g.drawLine(position.x+90,position.y+220,position.x+100,position.y+220);
	}

}