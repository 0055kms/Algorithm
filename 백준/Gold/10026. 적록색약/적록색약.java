import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {-1,1,0,0};
    static final int[] dy = {0,0,-1,1};
    static int N;
    static char[][] ground;
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        ground = new char[N][N];
        for (int i = 0; i<N; i++){
            String row = br.readLine();
            for (int j= 0; j<N; j++) ground[i][j] = row.charAt(j);
        }
        System.out.print(getA()+" ");
        for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                if (ground[i][j] == 'G') ground[i][j] = 'R';
            }
        }
        System.out.print(getA());
    }
    public static int getA(){
        int cnt  = 0;
        visited = new boolean[N][N];
        for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                if (!visited[i][j]){
                    cnt += 1; dfs(i,j);
                }
            }
        }
        return cnt;
    }
    public static void dfs(int x,int y){
        visited[x][y] = true;
        char color = ground[x][y];
        for (int k = 0; k<4; k++){
            int nx = x+ dx[k]; int ny = y+dy[k];
            if (0<=nx && 0<=ny && nx<N && ny<N && !visited[nx][ny] && ground[nx][ny] == color) dfs(nx,ny);
        }
    }
}

