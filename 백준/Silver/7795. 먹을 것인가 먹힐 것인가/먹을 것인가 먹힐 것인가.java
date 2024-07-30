import java.io.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        while (t-->0){
            int cnt = 0;
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            Integer[] A = new Integer[N];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i<N; i++) A[i] = Integer.parseInt(st.nextToken());
            int[] B = new int[M];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i<M; i++) B[i] = Integer.parseInt(st.nextToken());

            Arrays.sort(A,Collections.reverseOrder());
            Arrays.sort(B);
            int idx = M-1; // B[0] 부터 B[idx]까지 탐색

            for (int a: A){
                for (int i = 0; i<idx+1; i++){
                    if (B[i] < a) cnt += 1;
                    else{
                        idx = i-1;
                    }
                }
            }
            System.out.println(cnt);
        }
    }
}
/*
8 7 3 1 1
1 3 6
idx = 2;


 */