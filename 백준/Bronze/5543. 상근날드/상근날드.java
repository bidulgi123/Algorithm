import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int buger1 = sc.nextInt();
		int buger2 = sc.nextInt();	
		int buger3 = sc.nextInt();	
		int drink1= sc.nextInt();	
		int drink2 = sc.nextInt();
		
		System.out.println(Math.min(Math.min(buger1, buger2), buger3) + Math.min(drink1, drink2) -50);
		
		}
}
