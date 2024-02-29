import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main{
    static long min = 0;
    static int[] A;
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        A = new int[n];
        for (int i = n-1; i >= 0; i--){
            A[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i < n; i++){
            if (min < A[i]){
                min = A[i];
            } else {
                long cnt = min / A[i];
                if(min % A[i] != 0) cnt += 1;
                min = A[i] * cnt;
            }
        }
        System.out.println(min);
    }
}