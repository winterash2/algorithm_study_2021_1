package greedy;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


import static org.junit.Assert.assertEquals;


public class Juneui_숫자카드게임 {
    @Test
    public static void main(String[] args){
        List<Integer> firstInput = new ArrayList<>(Arrays.asList(3, 3));
        List<Integer[]> secondInput = new ArrayList<>(Arrays.asList(
                new Integer[][]{
                        {3, 1, 2},
                        {4, 1, 4},
                        {2, 2, 2}
                }
        ));
        assertEquals(solution(firstInput, secondInput), 2);

        firstInput = new ArrayList<>(Arrays.asList(2, 4));
        secondInput = new ArrayList<>(Arrays.asList(
                new Integer[][]{
                        {7, 3, 1, 8},
                        {3, 3, 3, 4}
                }
        ));
        assertEquals(solution(firstInput, secondInput), 3);
    }

    public static int solution(List<Integer> firstInput, List<Integer[]> secondInput){
        int answer = 0;
        final int N = firstInput.get(0);
        final int M = firstInput.get(1);

        for(int i = 0; i < N; ++i){
            int minVal = Collections.min(Arrays.asList(secondInput.get(i)));
            answer = minVal > answer ? minVal : answer;
        }

        return answer;
    }
}
