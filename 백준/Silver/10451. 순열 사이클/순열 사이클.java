import java.io.*;
import java.util.*;

public class Main {
    static int[] ar;
    static boolean[] visited;
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        while (T --> 0){
            N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            ar = new int[N+1];
            visited = new boolean[N+1];
            for (int i = 1; i<N+1; i++){
                ar[i] = Integer.parseInt(st.nextToken());
            }
            System.out.println(getCycle());
        }
    }
    public static int getCycle() {
        int cycle = 0;
        for (int s= 1; s<N+1; s++){
            if (!visited[s]) {
                int cur = ar[s];
                while (true) {
                    if (visited[cur]) {
                        cycle++;
                        break;
                    }
                    visited[cur] = true;
                    cur = ar[cur];
                }
            }
        }
        return cycle;
    }
}

