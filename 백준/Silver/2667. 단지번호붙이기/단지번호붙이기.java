import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};
    static int N;
    static int[][] board;
    static boolean[][] visit;
    static int ans1 = 0;
    static PriorityQueue<Integer> ans2 = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        visit = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String row = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = (int) (row.charAt(j) - '0');
                if (board[i][j] == 0) visit[i][j] = true;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visit[i][j]) {
                    ans1++;
                    ans2.offer(bfs(i, j));
                }
            }
        }
        System.out.println(ans1);
        while (!ans2.isEmpty()) System.out.println(ans2.poll());
    }

    public static int bfs(int sx, int sy) {
        int cnt = 1;
        visit[sx][sy] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sx, sy});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int k = 0; k < 4; k++) {
                int nx = cur[0] + dx[k];
                int ny = cur[1] + dy[k];
                if (0 <= nx && 0 <= ny && nx <= N - 1 && ny <= N - 1 && !visit[nx][ny]) {
                    visit[nx][ny] = true;
                    queue.offer(new int[]{nx, ny});
                    cnt += 1;
                }
            }
        }
        return cnt;
    }
}
/*
순서대로탐색 -> 방문안한 곳 발견 -> bfs 하며 ans1 1증가 ans2 계산 후 업데이트 방문체크 계산
 */