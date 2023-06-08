import java.util.*;

public class Main
{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = 0;
		int s = 0;
        for(int i = 1; i < 5;i++ ){
            int a, b, total;
            a=sc.nextInt();
            b=sc.nextInt();
            total=s+b-a;
            s=total;
            if(s>t)
                t=s;
        }
        System.out.print(t);
	}
}