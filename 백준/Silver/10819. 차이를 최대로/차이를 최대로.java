import java.io.*;
import java.util.*;

public class Main{
    static int ans = Integer.MIN_VALUE;
    static int N;
    static int[] A;
    static ArrayList<Integer> arr = new ArrayList<>();

    static boolean[] Visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        Visited = new boolean[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        dfs(0);
        System.out.println(ans);
    }
    public static void dfs(int depth){
        if (depth == N){
            int sum = 0;
            for (int i = 0; i<N-1; i++){
                sum += Math.abs(arr.get(i)-arr.get(i+1));
                ans = Math.max(sum,ans);
            }
        }
        else{
            for (int i = 0; i<N; i++){
                if (!Visited[i]){
                    Visited[i] = true;
                    arr.add(A[i]);
                    dfs(depth+1);
                    arr.remove(arr.size()-1);
                    Visited[i] = false;
                }
            }
        }
    }
}