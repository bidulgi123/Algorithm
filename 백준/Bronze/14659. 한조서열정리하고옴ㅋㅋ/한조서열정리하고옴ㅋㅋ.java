
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc = new Scanner(System.in);
			int b = 0;
			int cnt = 0;
			int t = 0;
			int a = sc.nextInt();
			int[] intArray = new int[a];
			for(int i=0;i<a;i++) {
				int q = sc.nextInt();
				intArray[i] = q; 
			}
			for(int i=0;i<a;i++) {
				if(intArray[i]>b) {
					b=intArray[i];
					cnt=0;
				}
				else {
					cnt+=1;
					if (t<cnt) {
						t=cnt;
					}
				}
			}
			System.out.println(t);
		}

}