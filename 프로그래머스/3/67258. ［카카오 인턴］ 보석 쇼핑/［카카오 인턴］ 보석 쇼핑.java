import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        /*
        sp부터 ep까지가 현재 구간
        처음에는 둘다 0
        min_length 처음에 gem.length
        
        while(ep != gem.length-1)
        if 만족 x -> ep += 1
        else ->
            if 길이가 1 (ep-sp == 0) 이면 그냥 현재꺼 리턴
            else
                if 길이 < min_length 라면 (ep-sp+1 < min_length) -> min_length업데이트 + 정답배열 업데이트
                else pass
                    sp += 1
        gem.length-1 까지 가능
        */
        int[] answer = {};
        int ans_sp = 0; int ans_ep = 0;
        HashSet<String> set = new HashSet<>();
        HashMap<String,Integer> gemCount = new HashMap<>();
        for (int i = 0; i<gems.length; i++){
            set.add(gems[i]);
        }
        int min_length = gems.length+1;
        int gem_num = set.size();
        gemCount.put(gems[0], 1);
        
        int sp = 0; int ep = 0;
        while (ep != gems.length){
            if (gemCount.size() < gem_num) {
                ep += 1; if(ep == gems.length) break;
                gemCount.compute(gems[ep], (key, val) -> (val == null) ? 1 : val + 1);}
            else{
                if (ep - sp == 0) return new int[]{ep+1,ep+1};
                else{
                    if (ep-sp+1 < min_length){
                        min_length = ep-sp+1; ans_sp = sp; ans_ep = ep;
                    }
                    gemCount.computeIfPresent(gems[sp], (key, val) -> val > 1 ? val - 1 : null);
                    sp += 1;
                }
            }
        }
        
        return new int[]{ans_sp+1,ans_ep+1};
    }
}