import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    static final int MAX = 1000*10000;
    static int ans = MAX;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] r = new int[N][3]; int[][] g = new int[N][3]; int[][] b = new int[N][3]; //rgb는 처음 색 , [3]은 각각 현재 r,b,g의 각각 최소 비용
        int[][] A = new int[N][3];
        for (int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            A[i][0] = Integer.parseInt(st.nextToken());
            A[i][1] = Integer.parseInt(st.nextToken());
            A[i][2] = Integer.parseInt(st.nextToken());
        }
        r[0][1] = MAX; r[0][2] = MAX; r[0][0] = A[0][0];
        g[0][0] = MAX; g[0][2] = MAX; g[0][1] = A[0][1];
        b[0][0] = MAX; b[0][1] = MAX; b[0][2] = A[0][2];

        for(int i = 1; i<N; i++){

            r[i][0] = A[i][0] + Math.min(r[i-1][1],r[i-1][2]);
            r[i][1] = A[i][1] + Math.min(r[i-1][0],r[i-1][2]);
            r[i][2] = A[i][2] + Math.min(r[i-1][0],r[i-1][1]);
            g[i][0] = A[i][0] + Math.min(g[i-1][1],g[i-1][2]);
            g[i][1] = A[i][1] + Math.min(g[i-1][0],g[i-1][2]);
            g[i][2] = A[i][2] + Math.min(g[i-1][0],g[i-1][1]);
            b[i][0] = A[i][0] + Math.min(b[i-1][1],b[i-1][2]);
            b[i][1] = A[i][1] + Math.min(b[i-1][0],b[i-1][2]);
            b[i][2] = A[i][2] + Math.min(b[i-1][0],b[i-1][1]);
        }
        ans = Math.min(ans,r[N-1][1]);
        ans = Math.min(ans,r[N-1][2]);
        ans = Math.min(ans,g[N-1][0]);
        ans = Math.min(ans,g[N-1][2]);
        ans = Math.min(ans,b[N-1][0]);
        ans = Math.min(ans,b[N-1][1]);
        System.out.println(ans);
    }
}