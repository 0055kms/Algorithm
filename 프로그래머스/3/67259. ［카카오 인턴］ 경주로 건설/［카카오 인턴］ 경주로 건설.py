"""
import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}

  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  """
"""
import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}

  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  """
"""
import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}

  import java.util.*;

class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static int[][][] costs; //[r][c][방향] = 최솟값
    
    class Node{
        int r,c,d;
        public Node(int r,int c,int d){
           this.r = r; this.c = c; this.d = d; 
        }
    }
    
    public int solution(int[][] board) {
        int N = board.length;
        costs = new int[N][N][4];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < 4; k++) {
                    costs[i][j][k] = Integer.MAX_VALUE;
                }
            }
        }

        for (int k = 0; k < 4; k++) {
            costs[0][0][k] = 0;
        }
        
        bfs(0, 0, board, N);
        return Arrays.stream(costs[N-1][N-1]).min().getAsInt();
    }
    
    public void bfs(int startR, int startC, int[][] board, int N) {
        Queue<Node> q = new LinkedList<>();
        if (board[0][1] == 0) {
            costs[0][1][0] = 100;
            q.offer(new Node(0, 1, 0));
        }
        if (board[1][0] == 0) {
            costs[1][0][2] = 100;
            q.offer(new Node(1, 0, 2));
        }
        
        while (!q.isEmpty()) {
            Node cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nR = cur.r + dir[d][0];
                int nC = cur.c + dir[d][1];
                if (0 <= nR && 0 <= nC && nR < N && nC < N && board[nR][nC] == 0) {
                    int nCost = (d == cur.d) ? costs[cur.r][cur.c][cur.d] + 100 : costs[cur.r][cur.c][cur.d] + 600;
                    if (nCost < costs[nR][nC][d]) {
                        costs[nR][nC][d] = nCost;
                        q.offer(new Node(nR, nC, d));
                    }
                }
            }
        }
    }
}
  """
