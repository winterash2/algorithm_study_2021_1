package simulation;

import static org.junit.Assert.assertEquals;

public class 시각 {
    public static void main(String[] args){
        int input = 5;
        assertEquals(solution(5), 11475);
    }
    public static int solution(int input){
        int answer = 0;
        for(int i = 0; i <= input; ++i){
            for(int j = 0; j < 60; ++j){
                for(int k = 0; k < 60; ++k){
                    if(String.valueOf(i).contains("3") || String.valueOf(j).contains("3") || String.valueOf(k).contains("3")) answer++;
                }
            }
        }

        return answer;
    }
}
