import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            int ans = 0;
            HashMap<Character, Integer> dic = new HashMap<>();
            int num = Integer.parseInt(br.readLine());
            if (num == 0) break;
            String str = br.readLine();
            int p1 = 0, p2 = 0;
            while (p2 < str.length()) {
                if (dic.size() <= num) {
                    char c = str.charAt(p2);
                    dic.put(c, dic.getOrDefault(c, 0) + 1);
                    if (dic.size() <= num) ans = Math.max(ans, p2 - p1 + 1);
                    p2++;
                } else {
                    char c = str.charAt(p1);
                    if (dic.get(c) == 1) dic.remove(c);
                    else dic.put(c, dic.get(c) - 1);
                    p1++;
                }
            }
            System.out.println(ans);
        }
        br.close();
    }
}
