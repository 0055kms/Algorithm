import java.util.*;

class Solution {
    public int solution(int n) {
        
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i<n+1; i++){
            dp[i] = (dp[i-1] + dp[i-2]) %1000000007;;
        }
        return dp[n];
        
        /*
        이전 + 세로
        두개전 + 가로두개
        */
    }
}