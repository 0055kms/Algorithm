import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] dp = new int[1001][10];  //dp[수의 길이][맨앞 숫자(가장 작은 수)]  dp[i][j] = dp[i-1][j<= k <= 9 인 모든 j]
        for (int i = 0; i<10; i++){
            dp[1][i] = 1;
        }
        for (int i = 2; i<1001; i++){
            for (int j = 0; j<10; j++){
                for (int k = j; k<10; k++){
                    dp[i][j] += dp[i-1][k];
                    dp[i][j] %= 10007;
                }
                dp[i][j] %= 10007;
            }
        }
        System.out.println(Arrays.stream(dp[N]).sum() % 10007);

    }
}
