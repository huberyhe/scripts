public class Circle1 {
	//在类中增加一个main方法用于测试
	public static void main(String[] args) {
		Circle1 myCircle = new Circle1(5.0);
		System.out.println("The area of the circle of radius " + myCircle.radius + " is " + myCircle.getArea());
		Circle1 yourCircle = new Circle1();	
		System.out.println("The area of the circle of radius " + yourCircle.radius + " is " + yourCircle.getArea());
		yourCircle.radius = 100;
		System.out.println("The area of the circle of radius " + yourCircle.radius + " is " + yourCircle.getArea());
	}

	double radius;
	//构造方法1
	Circle1() {
		radius = 1.0;
	}
	//构造方法2
	Circle1(double newRadius) {
		radius = newRadius;
	}
	double getArea() {
		return radius * radius * Math.PI;
	}
}
