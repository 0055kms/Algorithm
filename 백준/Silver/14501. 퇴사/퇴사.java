import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] re = new int[N][2];
        int[] arr = new int[N+1];
        for(int i = 0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            re[i][0] = Integer.parseInt(st.nextToken());
            re[i][1] = Integer.parseInt(st.nextToken());
        }
        for(int i = 0; i<N; i++){
            //일수와 T 합쳐서 N 이하만
            int T = re[i][0]; int P = re[i][1];
            if (T + i <= N) arr[T+i] = Math.max(arr[T+i],arr[i]+P);
            arr[i+1] = Math.max(arr[i+1],arr[i]);
        }
        System.out.println(arr[N]);
    }
}