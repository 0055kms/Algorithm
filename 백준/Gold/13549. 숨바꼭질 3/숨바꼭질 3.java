import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int K;
    static int[] visit;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        if (N==K) {System.out.println(0); System.exit(0);}
        visit = new int[200001]; //  i 까지 도착할 때 최소 시간 저장, 더 작은 시간 들어올 때만 업데이트 후 큐에 추가
        Arrays.fill(visit,Integer.MAX_VALUE);
        bfs(N);
        System.out.println(visit[K]);
    }

    public static void bfs(int s) {
        visit[s] = 0;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{N,0}); // 위치 , 시간
        while (!queue.isEmpty()){
            int[] cur = queue.poll();
            int[] nxt1 = new int[]{cur[0]-1,cur[1]+1};
            int[] nxt2 = new int[]{cur[0]+1,cur[1]+1};
            int[] nxt3 = new int[]{cur[0]*2,cur[1]};
            if (0<=nxt1[0] && nxt1[0]<=200000 && nxt1[1]<visit[nxt1[0]]) {
                visit[nxt1[0]] = nxt1[1]; queue.offer(nxt1);
            }
            if (0<=nxt2[0] && nxt2[0]<=200000 && nxt2[1]<visit[nxt2[0]]) {
                visit[nxt2[0]] = nxt2[1]; queue.offer(nxt2);
            }
            if (0<=nxt3[0] && nxt3[0]<=200000 && nxt3[1]<visit[nxt3[0]]) {
                visit[nxt3[0]] = nxt3[1]; queue.offer(nxt3);
            }
        }
    }
}
