import java.io.*;
import java.util.*;

public class Main {
    static final int[] dx = {-1,1,0,0};
    static final int[] dy = {0,0,-1,1};
    static int ans = 0; //연쇄 수
    static char[][] board = new char[12][6];

    private static class Node{
        int x,y;
        public Node(int x, int y){
            this.x = x; this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 12; i++) {
            String line = br.readLine();
            for (int j = 0; j < 6; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        while (true) {
            if (bfs()) {
                ans += 1;
                down();
            } else break;
        }
        System.out.println(ans);
    }
    public static boolean bfs(){ //flag반환 flag = 연쇄
        boolean flag = false;
        boolean[][] visited = new boolean[12][6];
        for (int i = 0; i<12; i++){
            for (int j = 0; j<6; j++){
                if (!visited[i][j] && board[i][j] != '.'){ // 4방향 bfs 탐색해서 같은색 있다면 저장,방문체크 -> 만약 4개 이상이라면 전부다 .로 바꾸고 flag = true
                    List<Node> sames = new ArrayList<>();
                    Queue<Node> queue = new LinkedList<>();
                    char color = board[i][j];
                    visited[i][j] = true;
                    queue.offer(new Node(i,j));  sames.add(new Node(i,j));
                    while (!queue.isEmpty()){
                        Node now = queue.poll();
                        for (int k = 0; k<4; k++){
                            Node next = new Node(now.x+dx[k], now.y+dy[k]);
                            if(0<=next.x && next.x<12 && 0<=next.y && next.y<6 && !visited[next.x][next.y] && color == board[next.x][next.y]){
                                sames.add(next); visited[next.x][next.y] = true; queue.offer(next);
                            }
                        }
                    }
                    if (sames.size() >= 4){
                        flag = true;
                        for (Node n: sames){
                            board[n.x][n.y] = '.';
                        }
                    }

                }
            }
        }
        return flag;}

    public static void down(){
        for (int j = 0; j < 6; j++) {
            for (int i = 11; i >= 0; i--) {
                if (board[i][j] == '.') {
                    for (int k = i - 1; k >= 0; k--) {
                        if (board[k][j] != '.') {
                            board[i][j] = board[k][j];
                            board[k][j] = '.';
                            break;
                        }
                    }
                }
            }
        }
        }

    }

