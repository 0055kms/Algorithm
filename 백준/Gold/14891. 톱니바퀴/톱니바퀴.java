import java.io.*;
import java.util.*;

public class Main {
    static int[][] A;
    public static void main(String[] args)throws IOException{
        //[2] 가 3시  [6] 가 6시
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        A = new int[4][8];
        for (int i = 0; i<4; i++){
            String s = br.readLine();
            for (int j = 0; j<8; j++){
                A[i][j] = s.charAt(j) - 48;
            }
        }
        int k = Integer.parseInt(br.readLine());
        while (k-->0){
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            move(num-1,dir);
        }
        int ans = 0;
        for (int i = 0; i<4; i++){
            if (A[i][0] == 1){
                ans += (int)Math.pow(2,i);
            }
        }
        System.out.println(ans);
    }
    static void move(int num, int dir){
        if (num >= 1 && A[num][6] != A[num-1][2]) moveL(num-1,-dir);
        if (num <= 2 && A[num][2] != A[num+1][6]) moveR(num+1,-dir);
        rotate(num,dir);
    }
    static void moveL(int num, int dir){
        if (num >= 1 && A[num][6] != A[num-1][2]) moveL(num-1,-dir);
        rotate(num,dir);
    }
    static void moveR(int num, int dir){
        if (num <= 2 && A[num][2] != A[num+1][6]) moveR(num+1,-dir);
        rotate(num,dir);
    }
    static void rotate(int num,int dir) {
        if (dir == 1) {
            int tmp = A[num][7];
            for (int i = 7; i >= 1; i--) {
                A[num][i] = A[num][i - 1];
            }
            A[num][0] = tmp;
        } else {
            int tmp = A[num][0];
            for (int i = 0; i <= 6; i++) {
                A[num][i] = A[num][i + 1];
            }
            A[num][7] = tmp;
        }
    }
}
