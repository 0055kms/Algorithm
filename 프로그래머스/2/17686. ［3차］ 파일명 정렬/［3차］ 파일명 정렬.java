import java.util.*;
class Solution {
    private static class File implements Comparable<File> {
        String head; int num; String name;
        
        public File(String fileName){
            int sNumIdx = -1;
            for (int i = 0; i<fileName.length(); i++){
                if (Character.isDigit(fileName.charAt(i))){
                    sNumIdx = i; break;
                }    
            }
            int eNumIdx = -1;
            for (int i = sNumIdx; i<fileName.length(); i++){
                if (!Character.isDigit(fileName.charAt(i))){
                    eNumIdx = i; break;
                }
            }
            if (eNumIdx == -1){eNumIdx = fileName.length();}
            String head = fileName.substring(0,sNumIdx);
            String num = fileName.substring(sNumIdx,eNumIdx);
            
            this.head = head.toLowerCase();
            this.num = Integer.parseInt(num);
            this.name = fileName;
        }
        
        @Override
        public int compareTo(File file) {
            int headComparison = this.head.compareTo(file.head);
            if (headComparison != 0) {
                return headComparison;
            }
            return Integer.compare(this.num, file.num);
        }
    }
    public String[] solution(String[] files) {
        /*
        헤드 넘버 테일 로 나누고
        헤드 : 소문자로 변경 후 사전 순(오름차순)으로 정렬
        넘버 : 앞의 0제거하고 (수 자체가 0인 경우 예외처리) 오름차순 정렬  
        */
        List<File> sorted = new ArrayList<File>();
        for (int i = 0; i<files.length; i++){
            sorted.add(new File(files[i]));
        }
        Collections.sort(sorted);
        String[] answer = new String[files.length];
        for (int i = 0; i<files.length; i++){
            answer[i] = sorted.get(i).name;
        }
        return answer;
    }
}