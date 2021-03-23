import java.util.*;

class Result{
    int score;
    String domain;

    public Result(int score, String domain){
        this.score = score;
        this.domain = domain;
    }
}

class Solution {
    public String solution(String[] table, String[] languages, int[] preference) {
        String answer = "";

        // 테이블 생성
        HashMap<String, ArrayList<String>> myTable = new HashMap<>();
        StringTokenizer st;
        for(String row : table){
            st = new StringTokenizer(row);
            String name = st.nextToken();
            ArrayList<String> list = new ArrayList<>();
            myTable.put(name, list);
            for(int i = 0; i < 5; ++i){
                String lan = st.nextToken();
                myTable.get(name).add(lan);
            }
        }

        ArrayList<Result> results = new ArrayList<>();

        for(Map.Entry<String, ArrayList<String>> entry : myTable.entrySet()){
            ArrayList<String> value = entry.getValue();
            int totalScore = 0;
            for(int i = 0; i < languages.length; ++i){
                int index = value.indexOf(languages[i]);
                if(index != -1){
                    totalScore += (5 - index) * preference[i];
                }
            }
            results.add(new Result(totalScore, entry.getKey()));
        }

        Collections.sort(results, (a, b) -> {
            if(a.score == b.score){
                return a.domain.compareTo(b.domain);
            } else {
                return b.score - a.score;
            }
        });

        answer = results.get(0).domain;

        return answer;
    }
}