import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] A = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                A[i][j] = Integer.parseInt(line[j]);
            }
        }
        if (A[N-1][N-1] == 1){
            System.out.println(0); System.exit(0);
        }

        int[][] dir = {{0, 1}, {1, 1}, {1, 0}};
        int ans = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 1, 0});

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int curx = current[0];
            int cury = current[1];
            int curd = current[2];

            for (int i = 0; i < 3; i++) {
                if (curd == 0 && i == 2) continue;
                if (curd == 2 && i == 0) continue;

                int dx = dir[i][0];
                int dy = dir[i][1];
                int nx = curx + dx;
                int ny = cury + dy;

                if (nx >= N || ny >= N || A[nx][ny] == 1) {
                    continue;
                }
                if (i == 1 && (A[nx - 1][ny] == 1 || A[nx][ny - 1] == 1)) {
                    continue;
                }
                if (nx == N - 1 && ny == N - 1) {
                    ans++;
                } else {
                    q.add(new int[]{nx, ny, i});
                }
            }
        }
        System.out.println(ans);
    }
}
