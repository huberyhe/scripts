/*PrintCalender,使用Date类获取当前日期,或从命令行输入
 *
 */
import net.ocod.terminalinput.TerminalInput;
import java.util.Date;
public class PrintCalender {
	public static void main(String[] args) {
                if (args.length != 0) 
			printMonthForInput(args);
                else
			printMonthForDate();
	}
	static void printMonthForInput(String[] args) {
		for(int i = 0;i < args.length;i++) {
			String[] dateString = args[i].split("\\D");
			printMonth(Integer.parseInt(dateString[0]),Integer.parseInt(dateString[1]));
		}
	}
	static void printMonthForDate() {
		Date date = new Date();
		String timeStr = date.toString();
		System.out.println(timeStr);
		int year = Integer.parseInt(timeStr.substring(24));
		System.out.println("Enter full year (e.g.,2001):" + year);
		int month = getMonthNumber(timeStr.substring(4,7));
		System.out.println("Enter month in number between 1 and 12:" + month);
		printMonth(year,month);
	}
	static void printMonth(int year,int month) {
		printMonthTitle(year,month);
		printMonthBody(year,month);	
	}
	static void printMonthTitle(int year,int month) {
		System.out.println("------------------------------------------");
		System.out.println("             " + getMonthName(month) + " " +year);
		System.out.println("------------------------------------------");
		System.out.println("   Sun   Mon   Tue   Wed   Thu   Fri   Sat");
	}
	static int getMonthNumber(String monthStr) {
		int monthNumber = 0;
		switch(monthStr) {
			case "Jan":monthNumber = 1;break;
			case "Feb":monthNumber = 2;break;
			case "Mar":monthNumber = 3;break;
			case "Apr":monthNumber = 4;break;
			case "May":monthNumber = 5;break;
			case "Jun":monthNumber = 6;break;
			case "Jul":monthNumber = 7;break;
			case "Aug":monthNumber = 8;break;
			case "Sep":monthNumber = 9;break;
			case "Oct":monthNumber = 10;break;
			case "Nov":monthNumber = 11;break;
			case "Dec":monthNumber = 12;break;
			default:monthNumber = 0;
		}
		return monthNumber;
	}
	static String getMonthName(int month) {
		String monthName = null;
		switch(month) {
			case 1: monthName = "January";break;
			case 2: monthName = "February";break;
			case 3: monthName = "March";break;
			case 4: monthName = "April";break;
			case 5: monthName = "May";break;
			case 6: monthName = "June";break;
			case 7: monthName = "July";break;
			case 8: monthName = "August";break;
			case 9: monthName = "September";break;
			case 10: monthName = "October";break;
			case 11: monthName = "November";break;
			case 12: monthName = "December";break;
		}
		return monthName;
	}
	static void printMonthBody(int year,int month) {
		int startDay = getStartDay(year,month);
		int numberOfDaysInMonth = getNumberOfDaysInMonth(year,month);
		int i = 0;
		for(i = 0; i < startDay;i++) {
			System.out.print("      ");
		}
		for(i = 1; i <= numberOfDaysInMonth;i++){
			if(i < 10)
				System.out.print("     " + i);
			else
				System.out.print("    " + i);
			if((i + startDay) % 7 == 0)
				System.out.println();
		}
		System.out.println();
	}
	static int getStartDay(int year,int month) {
		int startDay1800 = 3;
		int totalNumberOfDays = getTotalNumberOfDays(year,month);
		return (totalNumberOfDays + startDay1800) % 7;
	}
	static int getTotalNumberOfDays(int year,int month) {
		int total = 0;
		for (int i = 1800;i < year;i++)
		if(isLeapYear(i))
			total = total + 366;
		else
			total = total + 365;
		for (int i = 1;i < month;i++)
			total = total + getNumberOfDaysInMonth(year,i);
		return total;
	}
	static int getNumberOfDaysInMonth(int year,int month) {
		if (month == 1 || month == 3 || month ==5 || month == 7 || month== 8 || month == 10 || month == 12)
			return 31;
		if (month == 4 || month == 6 || month == 9 || month == 11)
			return 30;
		if (month == 2) return isLeapYear(year) ? 29 : 28;
			return 0;
	} 
	static boolean isLeapYear(int year) {
		return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
	}
}

