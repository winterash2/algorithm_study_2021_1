package greedy;

import java.util.Arrays;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class Juneui_만들수없는금액 {
    public static void main(String[] args){
        int N = 5;
        int input[] = {3, 2, 1, 1, 9};
        assertThat(solution(N, input), equalTo(8));
        N = 3;
        input = new int[]{3, 5, 7};
        assertThat(solution(N, input), equalTo(1));
    }

    public static int solution(int N, int[] input){
        int answer = 0;

        Arrays.sort(input);
        for(int i = 1;; ++i){
            int ret = Arrays.binarySearch(input, i);
            if(ret >= 0) continue;

            int j = 0;
            for(j = 0; j < input.length; ++j){
                if(i < input[j]) {
                    break;
                }
            }
            int sum = 0;
            boolean makeCoin = false;
            for(int k = j - 1; k >= 0; --k){
                sum += input[k];
                if(sum == i) {
                    makeCoin = true;
                    break;
                }
                if(sum > i) sum -= input[k];
            }
            if(!makeCoin){
                answer = i;
                break;
            }
        }

        return answer;
    }
}
