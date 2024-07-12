import java.io.*;
import java.util.*;

public class Main {

    static int ans = 0;
    static int[] table;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        String parent = br.readLine().replace(" ","");
        parent += parent;
        parent = parent.substring(0,parent.length()-1);
        String child = br.readLine().replace(" ","");

        KMP(parent,child);
        int gcd = getGCD(ans,N);
        System.out.println(ans/gcd + "/" + N/gcd);
    }

    public static void makeTable(String str){
        table = new int[str.length()];
        int idx = 0;
        for (int i = 1; i<str.length(); i++){
            while (idx > 0 && str.charAt(i) != str.charAt(idx)){
                idx = table[idx-1];
            }
            if (str.charAt(i) == str.charAt(idx)){
                idx ++;
                table[i] = idx;
            }
        }
    }
    public static void KMP(String parent, String child){
        makeTable(child);
        int idx = 0;
        for (int i = 0; i<parent.length(); i++){
            while(idx >0 && parent.charAt(i) != child.charAt(idx)){
                idx = table[idx - 1];
            }
            if (parent.charAt(i) == child.charAt(idx)){
                if (idx == child.length()-1){
                    idx = table[idx];
                    ans ++;
                }
                else{
                    idx ++;
                }
            }
        }
    }

    public static int getGCD(int a, int b){
        while (b!= 0){
            int tmp = b; b = a%b; a= tmp;
        }
        return a;
    }
}
