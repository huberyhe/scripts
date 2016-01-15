//This aplication program prints Welcome to java!
//以下三个类用于控制台输入，其包含于包java.io中
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Welcome {
	public static void main(String[] args){
		System.out.print("Enter a double velue:");
		//Scanner scanner = new Scanner(System.in);
		//double d = scanner.nextDouble();
		double d = Double.parseDouble(readString("Enter a double value:"));
		int i = (int)d;
		System.out.println("Welcome to java!" + "i = " + i + ",d = " + d+ ".");
	}
	private static String readString(String prompt){
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = null;
		try{
			System.out.print(prompt);
			str = br.readLine();
		}catch (IOException e){
			e.printStackTrace();
		}
		return str;
	}
}


