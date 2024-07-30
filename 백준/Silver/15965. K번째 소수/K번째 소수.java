import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int k = Integer.parseInt(br.readLine());
        int N = 500001*20;
        int ans = 0;

        boolean[] sosu = new boolean[N+1];
        Arrays.fill(sosu,true);
        sosu[0] = false; sosu[1] = false;
        for (int i = 2; i*i<N+1; i++){
            if (sosu[i]){
                for (int j = i*2; j<N+1; j+=i){
                    sosu[j] = false;
                }
            }
        }

        List<Integer> list = new ArrayList<>();
        for (int i = 0; i<N+1; i++){
            if (sosu[i]) list.add(i);
        }

        System.out.println(list.get(k-1));
    }
}
