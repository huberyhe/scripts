package net.ocod.terminalinput;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class TerminalInput {
	public static String strInput(String tiShi) {
		try {
			BufferedReader strin = new BufferedReader(new InputStreamReader(System.in));	
			System.out.print(tiShi);
			String str = strin.readLine();
			return str;
		}catch (IOException e) {
			e.printStackTrace();
			return "";
		}
	}

	public static int intInput(String tiShi) {
		try {
			BufferedReader strin = new BufferedReader(new InputStreamReader(System.in));
			System.out.print(tiShi);
			String str = strin.readLine();
			int intX = Integer.parseInt(str);
			return intX;
		}catch (IOException e){
			e.printStackTrace();
			return 0;
		}
	}
}
