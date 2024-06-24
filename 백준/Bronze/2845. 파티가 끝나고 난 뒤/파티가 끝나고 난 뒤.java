import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt(); 
        int d = sc.nextInt(); 
        int a = c * d;
        for (int i = 0; i<5; i++){
            int e = sc.nextInt();
            System.out.print(e-a+" ");
        }
    }
}