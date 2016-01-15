public class TestFileClass {
	public static void main(String[] args){
		java.io.File file = new java.io.File("image/us.gif");
		System.out.println("Does it exist? " + file.exists());
		System.out.println("Absolute path is " + file.getAbsolutePath());
		System.out.println("Last modefied on " + new java.util.Date(file.lastModified()));
	}
}
