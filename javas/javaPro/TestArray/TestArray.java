import javax.swing.JOptionPane;
public class TestArray {
	public static void main(String[] args) {
		final int TOTAL_NUMBERS = 6;
		int[] numbers = new int[TOTAL_NUMBERS];
		for (int i = 0;i < numbers.length;i++){
			String numString = JOptionPane.showInputDialog(
				"Enter a number:");
			numbers[i] = Integer.parseInt(numString);
		}
		int max = numbers[0];
		for (int i = 1;i < numbers.length;i++){
			if (max < numbers[i]){
				max = numbers[i];
			}
		}
		int count = 0;
		for (int i = 0;i < numbers.length;i++){
			if (numbers[i]==max) count++;
		}
		String output = "The array is ";
		for (int i = 0;i < numbers.length;i++){
			output += numbers[i] + " ";
		}
		output += "\nThe largest number is " + max;
		output += "\nThe occurrence count of the largest number is " + count;
		JOptionPane.showMessageDialog(null,output);
	}
}
