import java.io.*;
import java.util.*;

public class Main {
    static int[] table;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String A = br.readLine();
        A += A;
        A = A.substring(0,A.length()-1);
        String B = br.readLine();
        KMP(A,B);
        System.out.println(ans);
    }
    static void makeTable(String child) {
        table = new int[child.length()];
        int i=0;
        for(int j=1; j<child.length(); j++) {
            while(i>0 && child.charAt(j) != child.charAt(i)) i = table[i-1]; //불일치
            if(child.charAt(j) == child.charAt(i)) table[j] = ++i; //일치
        }
    }
    public static void KMP(String parent, String child){
        makeTable(child);
        int i = 0;
        for (int j = 0; j<parent.length(); j++){
            while(i >0 && parent.charAt(j) != child.charAt(i)) i = table[i - 1];
            if (parent.charAt(j) == child.charAt(i)){
                if (i == child.length()-1){ i = table[i]; ans += 1;} //j-i 인덱스에서 매치
                else i ++;
            }
        }
    }
}

