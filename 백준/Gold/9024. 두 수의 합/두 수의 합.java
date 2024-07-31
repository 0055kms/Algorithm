import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T-->0){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int [] ar = new int[n];
            for (int i = 0; i<n; i++) ar[i] = Integer.parseInt(st.nextToken());
            Arrays.sort(ar);
            int sp = 0; int ep = n-1;
            int min_val = Integer.MAX_VALUE;
            int min_ans = 0;
            while (sp < ep){
                int sum= ar[ep]+ar[sp];
                int tmp = Math.abs(sum-k);
                if (tmp < min_val){
                    min_val = tmp;
                    min_ans = 1;
                }
                else if (tmp == min_val){
                    min_ans += 1;
                }

                if(sum > k) ep -= 1;
                else if (sum <k) sp += 1;
                else {
                    sp += 1;
                    ep -=1;
                }
            }
            System.out.println(min_ans);
        }
    }
}
