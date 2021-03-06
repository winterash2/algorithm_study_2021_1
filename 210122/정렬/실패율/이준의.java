import java.util.*;

class Rate implements Comparable<Rate>{
    int index;
    double rate;
    public Rate(int index, double rate){
        this.index = index;
        this.rate = rate;
    }

    @Override
    public int compareTo(Rate o) {
        if(this.rate == o.rate){
            return this.index - o.index;
        }
        // Double형을 대소비교하여 -1, 0, 1 로 반환해줌
        return Double.compare(o.rate, this.rate);
    }
}

class Solution {
    public int[] solution(int n, int[] stages) {
        int[] answer = new int[n];
        Rate[] rates = new Rate[n];
        int challengers = stages.length;
        for(int stage = 1; stage <= n; ++stage){
            int count = 0;
            for(int i = 0; i < stages.length; ++i){
                if(stages[i] == stage) count++;
            }
            double fail = 0.0;
            // 해당스테이지에 도전자가 없는경우 실패율 0처리
            if(challengers != 0){
                fail = (double) count / challengers;
            }
            rates[stage - 1] = new Rate(stage, fail);
            challengers -= count;
        }
        Arrays.sort(rates);

        for(int i = 0; i < n; ++i){
            answer[i] = rates[i].index;
        }
        return answer;
    }
}