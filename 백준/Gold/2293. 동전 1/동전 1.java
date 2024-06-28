import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> arr = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] dp = new int[k+1]; dp[0] = 1;
        for (int i = 0; i<n; i++){
            arr.add(Integer.parseInt(br.readLine()));
        }
        for (int coin: arr){
            for (int i = 0; i<k+1; i++){
                if(i-coin >= 0){
                    dp[i] += dp[i-coin];
                }
            }
        }
        System.out.println(dp[k]);
    }
}
