import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, ArrayList<String>> category = new HashMap<>();
        for(String[] cloth : clothes){
            category.put(cloth[1], category.getOrDefault(cloth[1], new ArrayList<>()));
        }
        for(String[] cloth : clothes){
            category.get(cloth[1]).add(cloth[0]);
        }

        for(Map.Entry<String, ArrayList<String>> entries : category.entrySet()){
            answer *= entries.getValue().size() + 1;
        }
        return answer - 1;
    }
}