import javax.swing.*;
import java.awt.*;

public class TwoButtons {
	public static void main(String[] args) {
		JFrame frame = new JFrame();

		FlowLayout layout = new FlowLayout();
		frame.setLayout(layout);

		JButton jbtOK = new JButton("OK");
		JButton jbtCancel = new JButton("Cancel");
		frame.add(jbtOK);
		frame.add(jbtCancel);

		frame.setTitle("Window 1");
		frame.setSize(200,100);
		frame.setLocation(200,100);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
}
