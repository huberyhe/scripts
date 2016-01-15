import java.util.Scanner;
import java.io.Console;

public class TestScanner {
	public static void main(String args[]) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter an integer:");
		int intValue = scanner.nextInt();
		System.out.println("You entered the integer " + intValue);
		System.out.print("Enter a string without a space:");
		String string = scanner.next();
		System.out.println("You entered the string " + string);
		
		Console cin = System.console();
		String name = cin.readLine("Username:");
		char[] Password = cin.readPassword("Password:");
		String pass = "";
		for(char element:Password) {
			pass = pass + element;
		}
		System.out.println("Username:" + name + ",Password:" + pass);
	}
}
