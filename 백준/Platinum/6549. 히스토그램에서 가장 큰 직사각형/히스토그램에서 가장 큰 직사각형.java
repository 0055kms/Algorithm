import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            long ans = 0;
            Stack<Integer> stack = new Stack<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            if (N == 0) break;
            long[] val = new long[N + 1];
            for (int i = 0; i < N; i++) {
                val[i] = Long.parseLong(st.nextToken());
            }
            for (int i = 0; i <= N; i++) {
                while (!stack.isEmpty() && val[i] < val[stack.peek()]) {
                    long height = val[stack.pop()];
                    long width = stack.isEmpty() ? i : i - 1 - stack.peek();
                    ans = Math.max(ans, width * height);
                }
                stack.push(i);
            }
            System.out.println(ans);
        }
    }
}
