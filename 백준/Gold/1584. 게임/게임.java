import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {-1,1,0,0};
    static final int[] dy = {0,0,-1,1};

    private static class Node{
        int x,y;
        public Node(int x, int y){
            this.x = x; this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[501][501]; // 지역 종류 저장  0 안전 1 위험 2 죽음
        int[][] count = new int[501][501]; // 값 저장 , 더 작은 것이 올 때만 업데이트 후 큐에 넣음
        int N = Integer.parseInt(br.readLine());
        while (N-->0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            if (x2 < x1) {int tmp = x1; x1 =x2; x2 = tmp;}
            if (y2 < y1) {int tmp = y1; y1 =y2; y2 = tmp;}
            for (int i = x1; i<=x2; i++){
                for (int j = y1; j<=y2; j++){
                    board[i][j] = 1;
                }
            }
        }
        int M = Integer.parseInt(br.readLine());
        while (M-->0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            if (x2 < x1) {int tmp = x1; x1 =x2; x2 = tmp;}
            if (y2 < y1) {int tmp = y1; y1 =y2; y2 = tmp;}
            for (int i = x1; i<=x2; i++){
                for (int j = y1; j<=y2; j++){
                    board[i][j] = 2;
                }
            }
        }
        for (int i = 0; i <501; i++){
            for (int j = 0; j<501; j++) count[i][j] = Integer.MAX_VALUE;
        }
        count[0][0] = 0;

        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0,0));
        while (!q.isEmpty()){
            Node cur = q.poll();
            for (int k = 0; k<4; k++){
                int nx = cur.x + dx[k];
                int ny = cur.y + dy[k];
                if (nx<0 || nx>500 || ny <0 || ny >500 || board[nx][ny] == 2) continue;
                int val = count[cur.x][cur.y] + ((board[nx][ny] == 1)? 1: 0);
                if (val >= count[nx][ny]) continue;
                count[nx][ny] = val;
                q.offer(new Node(nx,ny));
            }
        }
        System.out.println((count[500][500] == Integer.MAX_VALUE)? -1: count[500][500]);
        }

    }

