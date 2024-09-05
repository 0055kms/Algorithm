import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[][] B;
    static int ans = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        B = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                B[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0, B);
        System.out.println(ans);
    }
    static void dfs(int depth, int[][] A) {
        if (depth == 5) {
            for (int[] row : A) {
                for (int value : row) {
                    ans = Math.max(ans, value);
                }
            }
            return;
        }
        dfs(depth + 1, up(Copy(A)));
        dfs(depth + 1, down(Copy(A)));
        dfs(depth + 1, right(Copy(A)));
        dfs(depth + 1, left(Copy(A)));
    }

    static int[][] Copy(int[][] origin) {
        int[][] copy = new int[origin.length][origin[0].length];
        for (int i = 0; i < origin.length; i++) {
            System.arraycopy(origin[i], 0, copy[i], 0, origin[i].length);
        }
        return copy;
    }

    static int[][] up(int[][] B) {
        for (int x = 0; x < N; x++) {
            int ptr = 0;
            for (int y = 1; y < N; y++) {
                if (B[y][x] != 0) {
                    int tmp = B[y][x];
                    B[y][x] = 0;
                    if (B[ptr][x] == 0) {
                        B[ptr][x] = tmp;
                    } else if (B[ptr][x] == tmp) {
                        B[ptr][x] = 2 * tmp;
                        ptr++;
                    } else {
                        ptr++;
                        B[ptr][x] = tmp;
                    }
                }
            }
        }
        return B;
    }

    static int[][] down(int[][] B) {
        for (int x = 0; x < N; x++) {
            int ptr = N - 1;
            for (int y = N - 2; y >= 0; y--) {
                if (B[y][x] != 0) {
                    int tmp = B[y][x];
                    B[y][x] = 0;
                    if (B[ptr][x] == 0) {
                        B[ptr][x] = tmp;
                    } else if (B[ptr][x] == tmp) {
                        B[ptr][x] = 2 * tmp;
                        ptr--;
                    } else {
                        ptr--;
                        B[ptr][x] = tmp;
                    }
                }
            }
        }
        return B;
    }

    static int[][] right(int[][] B) {
        for (int y = 0; y < N; y++) {
            int ptr = 0;
            for (int x = 1; x < N; x++) {
                if (B[y][x] != 0) {
                    int tmp = B[y][x];
                    B[y][x] = 0;
                    if (B[y][ptr] == 0) {
                        B[y][ptr] = tmp;
                    } else if (B[y][ptr] == tmp) {
                        B[y][ptr] = 2 * tmp;
                        ptr++;
                    } else {
                        ptr++;
                        B[y][ptr] = tmp;
                    }
                }
            }
        }
        return B;
    }

    static int[][] left(int[][] B) {
        for (int y = 0; y < N; y++) {
            int ptr = N - 1;
            for (int x = N - 2; x >= 0; x--) {
                if (B[y][x] != 0) {
                    int tmp = B[y][x];
                    B[y][x] = 0;
                    if (B[y][ptr] == 0) {
                        B[y][ptr] = tmp;
                    } else if (B[y][ptr] == tmp) {
                        B[y][ptr] = 2 * tmp;
                        ptr--;
                    } else {
                        ptr--;
                        B[y][ptr] = tmp;
                    }
                }
            }
        }
        return B;
    }
}