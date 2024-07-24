import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        long[] ar = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<N; i++) ar[i] = Long.parseLong(st.nextToken());
        long ans = 0; long ans_ = 0; long min_val = Long.MAX_VALUE;// 작은용액 큰용액  두용액합의 절댓값 최소
        int sp = 0; int ep = N-1; // 포인터들
        Arrays.sort(ar);

        while (sp != ep){
            long sum = ar[sp] + ar[ep];
            if (Math.abs(sum) < min_val){
                min_val = Math.abs(sum);
                ans = ar[sp]; ans_ = ar[ep];}
            if (sum > 0) ep -= 1;
            else sp += 1;
        }
        System.out.println(ans + " " + ans_);

    }
}
