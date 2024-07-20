import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // dp[i][j] i번째 포도주 까지 j번째 누적일 때 최대값
        int n = Integer.parseInt(br.readLine());
        int[] ar = new int[n];
        int[][] dp = new int[n][3];
        for (int i = 0; i<n; i++) ar[i] = Integer.parseInt(br.readLine());
        if (n <= 2){
            int ans_ = 0;
            for (int i: ar) ans_ += i;
            System.out.print(ans_);
            System.exit(0);
        }
        dp[0][0] = 0; dp[0][1] = ar[0];
        dp[1][0] = ar[0]; dp[1][1] = ar[1]; dp[1][2] = ar[0] + ar[1];

        for (int i = 2; i<n; i++){
            dp[i][0] = Arrays.stream(dp[i-1]).max().orElseThrow();
            dp[i][1] = dp[i-1][0] + ar[i];
            dp[i][2] = dp[i-1][1] + ar[i];
        }
        System.out.print(Arrays.stream(dp[n-1]).max().orElseThrow());

    }

}

