import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        // 가운데 곰곰 -> 곰곰 이김
        // (1,2) -> 총총 이김
        System.out.println((N==2 && M==1)||(N==1 && M==2)?"ChongChong": "GomGom");
    }
}
