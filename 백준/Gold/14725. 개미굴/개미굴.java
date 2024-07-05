import java.io.*;
import java.util.*;

public class Main {
    private static class Node{
        Map<String,Node> childNode = new TreeMap<>();
        boolean isEnd;
    }

    private static class Trie{
        Node rootNode = new Node();

        void insert(String[] strArray){
            Node curNode = this.rootNode;
            for (String str: strArray){
                curNode = curNode.childNode.computeIfAbsent(str,key -> new Node());
            }
            curNode.isEnd = true;
        }

        void print(Node node, int depth){
            for (String key : node.childNode.keySet()) {
                for (int i = 0; i < depth; i++) {
                    System.out.print("--");
                }
                System.out.println(key);
                print(node.childNode.get(key), depth + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Trie trie = new Trie();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int K = Integer.parseInt(st.nextToken());
            String[] StringArray = new String[K];
            int idx = 0;
            while (st.hasMoreTokens()) {
                StringArray[idx++] = st.nextToken();
            }
            trie.insert(StringArray);
        }

        trie.print(trie.rootNode, 0);
    }
}
