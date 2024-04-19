import java.io.*;
import java.util.*;


public class Main {
    static ArrayList<String> brk = new ArrayList<>();
    static int ans = Integer.MAX_VALUE;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        ans = Math.abs(100-N);
        int M = Integer.parseInt(br.readLine());
        if (M > 0){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int i = 0; i<M; i++) {
                String k = st.nextToken();
                brk.add(k);
            }
        }
        for (int num = 0; num < 1000001; num++) {
            update(String.valueOf(num));
        }
        System.out.println(ans);
    }
    public static void update(String num_str){
        for (char c : num_str.toCharArray()) {
            if (brk.contains(String.valueOf(c))){
                return;
            }
        }
        ans = Math.min(num_str.length() + Math.abs(Integer.parseInt(num_str)-N), ans);
    }
}
