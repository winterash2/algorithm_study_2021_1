package greedy;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class Juneui_볼링공고르기 {
    public static void main(String[] args){
        int N = 5;
        int M = 3;
        int[] input = {1, 3, 2, 3, 2};
        assertThat(solution(N, M, input), equalTo(8));
        N = 8; M = 5;
        input = new int[]{1, 5, 4, 3, 2, 4, 5, 2};
        assertThat(solution(N, M, input), equalTo(25));
    }
    public static int solution(int N, int M, int[] input){
        int answer = 0;
        for(int i = 0; i < N; ++i){
            for(int j = i + 1; j < N; ++j){
                if(input[i] != input[j]) answer++;
            }
        }
        return answer;
    }
}