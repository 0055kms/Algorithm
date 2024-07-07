import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<int[]> stack = new Stack<>();
        int N = Integer.parseInt(br.readLine());
        long ans = 0;
        int[] ar = new int[N];
        int idx = 0;
        while (idx != N) {
            ar[idx++] = Integer.parseInt(br.readLine());
        }

        stack.add(new int[]{ar[0], 1});
        for (int i = 1; i < N; i++) {
            int cur = ar[i];
            int count = 1;

            while (!stack.isEmpty() && cur > stack.peek()[0]) {
                ans += stack.pop()[1];
            }

            if (!stack.isEmpty() && cur == stack.peek()[0]) {
                count += stack.pop()[1];
                ans += count - 1;
            }

            if (!stack.isEmpty()) {
                ans += 1;
            }

            stack.add(new int[]{cur, count});
        }
        System.out.println(ans);
    }
}
