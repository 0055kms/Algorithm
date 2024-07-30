import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int ans = 0;

        boolean[] sosu = new boolean[N+1];
        Arrays.fill(sosu,true);
        sosu[0] = false; sosu[1] = false;
        for (int i = 2; i<N+1; i++){
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

        int sum = 0; int sp = 0; int ep = 0; //sp부터 ep까지의 합 = sum

            while(true) {
                if(sum >= N ) sum -= list.get(sp++);
                else if(ep == list.size()) break;
                else sum += list.get(ep++);
                if(N==sum) ans++;
            }

        System.out.println(ans);
    }
}
