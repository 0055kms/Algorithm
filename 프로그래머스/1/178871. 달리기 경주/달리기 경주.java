import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String,Integer> rank = new HashMap<>();
        for (int i = 0; i<players.length; i++){
            rank.put(players[i],i);
        }
        
        for (String front : callings){
            int front_idx = rank.get(front);
            int back_idx = front_idx-1; String back = players[back_idx];
            rank.put(back,front_idx); rank.put(front,back_idx);
            players[back_idx] = front; players[front_idx] = back;
        } 
        return players;
    }
}