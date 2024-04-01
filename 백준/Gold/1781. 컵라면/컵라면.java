import java.io.*;
import java.util.*;

public class Main{
    static int N;
    public static void main(String[] args) throws IOException{
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        int[][] A = new int[N][2];
        for (int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<2; j++){
                A[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        Arrays.sort(A, (a, b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i<N; i++){
            pq.add(A[i][1]);
            while (A[i][0] < pq.size()) pq.poll();
        }
        int ans = 0;
        for (int n : pq) ans += n;
        System.out.println(ans);

    }
}