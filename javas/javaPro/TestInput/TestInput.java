import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class TestInput {
	public static void main(String[] args) {
		try {
			BufferedReader strin = new BufferedReader(new InputStreamReader(System.in));	
			System.out.print("请输入一个字符串：");
			String str = strin.readLine();
			System.out.println("字符串是：" + str);
		}catch (IOException e) {
			e.printStackTrace();
		}
	}
}
