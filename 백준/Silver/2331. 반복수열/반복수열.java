import java.io.*;
import java.util.*;

public class Main {
    static int A,P;
    public static void main(String[] args) throws IOException{
        Set<Integer> set = new HashSet<>();
        List<Integer> numbers = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        int cur = A;
        while (true){
            if (set.contains(cur)){
                break;
            }
            else{
                set.add(cur); numbers.add(cur);
                cur = nextNum(cur);
            }
        }
        System.out.println(numbers.indexOf(cur));
        /*
        만약 지금까지 나온 것과 같은 수가 나옴 -> 그 수를 저장하고 리스트 앞에서부터 인덱스 탐색
         */
    }
    public static int nextNum(int Num){
        String strNum = Integer.toString(Num);
        int result = 0;
        for(char c: strNum.toCharArray()){
            result += (int)Math.pow(c-48,P);
        }
        return result;
    }
}

