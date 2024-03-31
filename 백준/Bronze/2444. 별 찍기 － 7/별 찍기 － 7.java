import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a = 0;
        while (a++ < N){
            for (int i = 0; i<N-a; i++)System.out.print(" ");
            for (int i = 0; i<2*a-1; i++)System.out.print("*");
            System.out.println();
        }
        a-=1;
        while (a-- > 1){
            for (int i = 0; i<N-a; i++)System.out.print(" ");
            for (int i = 0; i<2*a-1; i++)System.out.print("*");
            System.out.println();
        }

    }
}