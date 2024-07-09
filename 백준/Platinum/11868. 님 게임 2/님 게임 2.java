import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] ar = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i<N; i++){
            ar[i] = Integer.parseInt(st.nextToken());
        }

        int kooWin = 0;
        for (int i: ar){
            kooWin ^= i;
        }
        if (kooWin == 0) {
            System.out.println("cubelover");
        } else {
            System.out.println("koosaga");
        }



        /*
        내 차례에 0 만들려면 -> 모든 더미 중 같은 값 없게
         */
    }
}
