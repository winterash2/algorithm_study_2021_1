package greedy;

import org.junit.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class Juneui_모험가길드 {
    @Test
    public static void main(String[] args){
        int[] input = new int[]{2, 3, 1, 2, 2};
        assertThat(solution(5, input), equalTo(2));
        input = new int[]{1, 1, 1, 1, 1};
        assertThat(solution(5, input), equalTo(5));
        input = new int[]{1, 2, 3, 4, 5};
        assertThat(solution(5, input), equalTo(1));
        input = new int[]{1};
        assertThat(solution(1, input), equalTo(1));
        input = new int[]{2};
        assertThat(solution(1, input), equalTo(0));
        input = new int[]{5, 5, 5, 5, 5};
        assertThat(solution(5, input), equalTo(1));
    }

    public static int solution(int n, int[] input){
        int answer = 0;
        Arrays.sort(input);

        for(int i = 0; i < n; ++i){
            int minGroup = input[i];
            boolean isGroup = true;
            for(int k = i + 1; k < i + minGroup; ++k){
                isGroup = false;
                if(k >= input.length) break;
                if(minGroup < input[k]) break;
                if(k == i + minGroup - 1) {
                    i = k + 1;
                    isGroup = true;
                    break;
                }
            }
            if(isGroup) {
                answer++;
            }
        }

        return answer;
    }
}
