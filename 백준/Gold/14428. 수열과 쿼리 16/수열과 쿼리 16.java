import java.io.*;
import java.util.*;

public class Main {
    static int treeHeight = 0, treeSize;
    static int[] tree;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        arr = new int[N + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        while ((1 << treeHeight) < N) {
            treeHeight++;
        }
        treeSize = 1 << (treeHeight + 1);
        tree = new int[treeSize];

        init(1, 1, N);

        int M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());
            if (command == 1) {
                int idx = Integer.parseInt(st.nextToken());
                int val = Integer.parseInt(st.nextToken());
                update(1, 1, N, idx, val);
            } else if (command == 2) {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                sb.append(query(1, 1, N, left, right)).append("\n");
            }
        }

        System.out.print(sb);
    }

    static int init(int node, int start, int end) {
        if (start == end) {
            return tree[node] = start;
        }
        int mid = (start + end) / 2;
        int leftIndex = init(node * 2, start, mid);
        int rightIndex = init(node * 2 + 1, mid + 1, end);
        return tree[node] = (arr[leftIndex] <= arr[rightIndex]) ? leftIndex : rightIndex;
    }

    static int update(int node, int start, int end, int idx, int val) {
        if (idx < start || idx > end) {
            return tree[node];
        }
        if (start == end) {
            arr[idx] = val;
            return tree[node] = start;
        }
        int mid = (start + end) / 2;
        int leftIndex = update(node * 2, start, mid, idx, val);
        int rightIndex = update(node * 2 + 1, mid + 1, end, idx, val);
        return tree[node] = (arr[leftIndex] <= arr[rightIndex]) ? leftIndex : rightIndex;
    }

    static int query(int node, int start, int end, int left, int right) {
        if (right < start || left > end) {
            return -1;
        }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        int leftIndex = query(node * 2, start, mid, left, right);
        int rightIndex = query(node * 2 + 1, mid + 1, end, left, right);

        if (leftIndex == -1) return rightIndex;
        if (rightIndex == -1) return leftIndex;
        return (arr[leftIndex] <= arr[rightIndex]) ? leftIndex : rightIndex;
    }
}
