import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int time = 0;
        final int[] dx = {-1,1,0,0};
        final int[] dy = {0,0,-1,1};
        st =new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        Queue<int[]> et = new LinkedList<>();
        Queue<int[]> tmp = new LinkedList<>();
        int[][] board = new int[N][M];
        for (int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<M; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) tmp.offer(new int[]{i,j});
            }
        }
        while (true) {
            et = new LinkedList<>(tmp);
            tmp.clear();
            while (!et.isEmpty()) {
                int[] now = et.poll();
                for (int k = 0; k < 4; k++) {
                    int nx = now[0] + dx[k];
                    int ny = now[1] + dy[k];
                    if (0 <= nx && nx <= N - 1 && 0 <= ny && ny <= M - 1 && board[nx][ny] == 0) {
                        board[nx][ny] = 1;
                        tmp.offer(new int[]{nx, ny});
                    }
                }
            }
            if (tmp.isEmpty()) break;
            time ++;
        }

        boolean flag = true;
        for (int i = 0; i<N; i++){
            for (int j = 0; j<M; j++){
                if (board[i][j] == 0) flag = false;
            }
        }
        System.out.println(flag? time: -1);

    }
}
