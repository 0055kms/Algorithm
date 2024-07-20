import java.io.*;
import java.util.*;

public class Main {

    static class Node {
        Node[] childNode = new Node[2];
    }

    static class Trie {
        Node root;

        public Trie() {
            root = new Node();
        }

        public void insert(int num) {
            Node cur = root;
            for (int i = 30; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (cur.childNode[bit] == null) {
                    cur.childNode[bit] = new Node();
                }
                cur = cur.childNode[bit];
            }
        }

        public int findMaxXOR(int num) {
            Node cur = root;
            int xorValue = 0;
            for (int i = 30; i >= 0; i--) {
                int bit = (num >> i) & 1;
                if (cur.childNode[1 - bit] != null) {
                    xorValue |= (1 << i);
                    cur = cur.childNode[1 - bit];
                } else {
                    cur = cur.childNode[bit];
                }
            }
            return xorValue;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Trie trie = new Trie();
        for (int num : nums) {
            trie.insert(num);
        }

        int maxXOR = 0;
        for (int num : nums) {
            maxXOR = Math.max(maxXOR, trie.findMaxXOR(num));
        }

        System.out.println(maxXOR);
    }
}
