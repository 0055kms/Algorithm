import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int min = Integer.MAX_VALUE;
        /*
            최소 =
            for (int a: A)
            for: a-4 a-3 a-2 a-1 a  ~  a a+1 a+2 a+3 a+4 까지  총 5번
                cnt = 필요한 수들 중 배열에 없는 수 개수
                최소 = min(cnt,최소)
         */
        int []A = new int[N];
        for (int i = 0; i<N; i++) A[i] = Integer.parseInt(br.readLine());
        Arrays.sort(A);
        for (int a: A){
            for (int m = -4; m<=0; m++){
                int cnt = 0;
                for (int n = 0; n<=4; n++){
                    if (!contains(A,a+m+n)) cnt += 1;
                }
                min = Math.min(min,cnt);
            }
        }
        System.out.println(min);
    }
    public static boolean contains(int[] A, int a){
        for (int x: A){
            if (x == a) return true;
        }
        return false;
    }
}
