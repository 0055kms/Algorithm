import java.io.*;
import java.util.*;

public class Main {
    static int[] table;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String str = br.readLine();
        makeTable(str);
        System.out.println(N-table[N-1]);

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
                if (i == child.length()-1) i = table[i]; //j-i 인덱스에서 매치
                else i ++;
            }
        }
    }
}

