import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static ArrayList<Integer>[] graph;
    static int[] parent;
    static boolean[] visited;
    static int[] dCheck;
    static boolean[] rootCheck;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());
        while (T-->0){
            N = Integer.parseInt(br.readLine());
            graph = new ArrayList[N+1];
            for (int i = 0; i<N+1; i++) graph[i] = new ArrayList<>();
            visited = new boolean[N+1];
            parent = new int[N+1];
            dCheck = new int[N+1];
            rootCheck = new boolean[N+1]; Arrays.fill(rootCheck,true);
            for (int k = 0; k<N-1; k++){
                st = new StringTokenizer(br.readLine());
                int p = Integer.parseInt(st.nextToken()); int c = Integer.parseInt(st.nextToken());
                parent[c] = p;
                graph[c].add(p); graph[p].add(c);
                rootCheck[c] = false;
            }

            int root = -1;
            for (int i = 1; i<N+1; i++){
                if (rootCheck[i]){
                    root = i; break;
                }
            }
            dfs(root,0);

            st = new StringTokenizer(br.readLine());
            int node = Integer.parseInt(st.nextToken());
            int deepNode = Integer.parseInt(st.nextToken());
            if (dCheck[node] > dCheck[deepNode]){
                int tmp = node;
                node = deepNode;
                deepNode = tmp;
            }
            while (dCheck[node]!=dCheck[deepNode]) deepNode = parent[deepNode];
            while (node != deepNode) {
                node = parent[node]; deepNode = parent[deepNode];
            }
            System.out.println(node);

            /*
            1. 루트노드 찾기
            2. parent에 부모 저장 및 graph에 양방향 에지 저장
            3. 루트노드부터 dfs 하면서 노드들 깊이 계산 - dCheck에
            4. parent로 깊이 맞추기 + 공통 조상 찾기
             */


        }
    }

    public static void dfs(int n, int depth) {
        visited[n] = true;
        dCheck[n] = depth;
        for (int next : graph[n]) if (!visited[next]) dfs(next, depth + 1);
    }
}
