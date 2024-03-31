import java.io.*;
import java.util.*;

public class Main{
    static int N,M,ans = 0;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        PriorityQueue<Integer> plusQ = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minusQ = new PriorityQueue<>();
        st = new StringTokenizer(br.readLine());
        int max = Integer.MIN_VALUE;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<N; i++){
            int t = Integer.parseInt(st.nextToken());
            max = Math.max(max,Math.abs(t));
            if (t > 0)plusQ.add(t); else minusQ.add(t);
        }

        int cnt = 0;
        while (!plusQ.isEmpty()){
            int now = plusQ.poll();
            if (cnt == 0) ans += 2*now;
            cnt += 1;
            if (cnt == M) cnt = 0;
        }
        cnt = 0;
        while (!minusQ.isEmpty()){
            int now = -minusQ.poll();
            if (cnt == 0) ans += 2*now;
            cnt += 1;
            if (cnt == M) cnt = 0;
        }
        System.out.println(ans-max);
// 39 37 29 28 6   0   2 11
        // 2 + 11 + 10 + 6

    }
}