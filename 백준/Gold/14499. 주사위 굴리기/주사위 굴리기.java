import java.io.*;
import java.util.*;


public class Main {
    static int N, M, x, y , K;
    static int [][] map;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};
    static int [] dice = new int[7];
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        for (int i = 0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j<M; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        st = new StringTokenizer(br.readLine());
        for (int i = 0; i<K; i++){
            int now = Integer.parseInt(st.nextToken()) - 1;
            y += dy[now]; x += dx[now];
            if (y < 0 || y > M-1 || x <0 || x > N-1){
                y -= dy[now]; x -= dx[now]; continue;
            }
            move(now);
            if (map[x][y] == 0) map[x][y] = dice[6];
            else{
                dice[6] = map[x][y];
                map[x][y] = 0;
            }
            System.out.println(dice[1]);



        }

    }
    public static void move(int cmd){
        int tmp = dice[1];
        switch (cmd){
            case 0:
                dice[1] = dice[4];
                dice[4] = dice[6];
                dice[6] = dice[3];
                dice[3] = tmp;
                break;
            case 1:
                dice[1] = dice[3];
                dice[3] = dice[6];
                dice[6] = dice[4];
                dice[4] = tmp;
                break;

            case 2:
                dice[1] = dice[2];
                dice[2] = dice[6];
                dice[6] = dice[5];
                dice[5] = tmp;
                break;

            case 3:
                dice[1] = dice[5];
                dice[5] = dice[6];
                dice[6] = dice[2];
                dice[2] = tmp;
                break;

        }
    }
}
    /*
    바닥은 6이다

         (남)
         2
  (서) 4 1 3 (동)
         5(북)
         6(바닥)

    (prev->new)
    동 : 1->3  3->6  6->4  4->1
    tmp = d[1]; d[1] = d[4]; d[4] = d[6]; d[6] = d[3]; d[3] = tmp;
    서 : 3->1 1->4  4->6  6->3
    tmp = d[1]; d[1] = d[3]; d[3] = d[6]; d[6] = d[4]; d[4] = tmp;
    북 : 1->5 5->6 6->2 2->1
    tmp = d[1]; d[1] = d[2]; d[2] = d[6]; d[6] = d[5]; d[5] = tmp;
    남 : 5->1 6->5 2->6 1->2
    tmp = d[1]; d[1] = d[5]; d[5] = d[6]; d[6] = d[2]; d[2] = tmp;

     */


