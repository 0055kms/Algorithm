import java.io.*;
import java.util.*;

public class Main {
    static int ans = 0;
    static int[] parent;
    static class Node implements Comparable<Node>{
        int s,e,w;
        public Node(int s, int e, int w){
            this.s = s; this.e = e; this.w = w;
        }
        @Override
        public int compareTo(Node n){
            return this.w - n.w;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        List<Node> edges = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        for (int i = 0; i<E; i++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            edges.add(new Node(s,e,w));
        }
        parent = new int[V+1];
        for (int i = 0; i<V+1; i++) parent[i] = i;
        Collections.sort(edges);

        for(Node n: edges){
            if (find(n.s) == find(n.e)) continue;
            ans += n.w;
            union(n.s,n.e);
        }
        System.out.print(ans);
    }

    public static int find(int a){
        if (parent[a] == a) return a;
        else return parent[a] = find(parent[a]);
    }

    public static void union(int a, int b){
        a = find(a);
        b = find(b);
        if (a!=b) parent[b] = a;
    }

}

