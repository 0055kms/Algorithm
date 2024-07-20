import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static int[] parent;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 점개수
        int m = Integer.parseInt(st.nextToken()); // 진행 차례 수
        parent = new int[n];
        for (int i = 0; i<n; i++) parent[i] = i;
        /*
        사이클 완성 = find 했는데 같다
        cnt 로 진헹 순서 체크하고 사이클 완성되면 ans = cnt
         */
        int cnt = 0;
        while (m --> 0){
            cnt ++;
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            if (find(s) == find(e)) {ans = cnt; break;}
            union(s,e);
        }
        System.out.print(ans);

    }
    public static int find(int a){
        if (parent[a] == a) return a;
        else return parent[a] = find(parent[a]);
    }

    public static void union(int a,int b){
        a = find(a);
        b = find(b);
        if (a!=b) parent[b] = a;
    }

}

