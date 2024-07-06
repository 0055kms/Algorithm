import java.util.*;
class Solution {
    private static final int[][] dir = {{0,1},{0,-1},{1,0},{-1,0}};
    private static boolean[][][] visited = new boolean[11][11][4];
    private static class Node{
        int r,c;
        public Node(int r, int c){
            this.r = r; this.c = c;
        }
    }
    private static Map<Character,Integer> map = new HashMap<>(){{
    put('U',0); put('D',1); put('R',2); put('L',3);}};
    
    public int solution(String dirs) {
        int answer = 0;
        Node cNode = new Node(5,5);
        for (char cmd: dirs.toCharArray()){
            int d = map.get(cmd);
            Node pNode = new Node(cNode.r,cNode.c);
            if (0 <= cNode.r + dir[d][0] && cNode.r + dir[d][0] <= 10
               && 0 <= cNode.c + dir[d][1] && cNode.c + dir[d][1] <= 10){
            cNode.r += dir[d][0]; cNode.c += dir[d][1];
            if (visited[pNode.r][pNode.c][d] == false){
                visited[pNode.r][pNode.c][d] = true;
                visited[cNode.r][cNode.c][op(d)] = true;
                answer += 1;
                
            }
            }
            }
        return answer;
        }
    public int op(int cmd){
        int tmp = 0;
        switch(cmd){
            case 0:
                tmp = 1; break;
            case 1:
                tmp = 0; break;
            case 2:
                tmp = 3; break;
            case 3:
                tmp = 2; break;
        }
        return tmp;
    }
}
/*
길 체크 방법 : 3차원 배열 [r][c][방향] 시작과 끝 둘 다 체크 필요 크기 11 시작 인덱스 [5][5]
*/