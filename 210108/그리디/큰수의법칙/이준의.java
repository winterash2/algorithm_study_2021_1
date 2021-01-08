package greedy.problem1;

import java.util.*;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Juneui_큰수의법칙 {
    @Test
    public static void main(String[] args){
        List<Integer> firstInput = new ArrayList<>(Arrays.asList(5, 8, 3));
        List<Integer> secondInput = new ArrayList<>(Arrays.asList(2, 4, 5, 4, 6));
        assertEquals(solution(firstInput, secondInput), 46);

        firstInput = new ArrayList<>(Arrays.asList(5, 7, 2));
        secondInput = new ArrayList<>(Arrays.asList(3, 4, 3, 4, 3));
        assertEquals(solution(firstInput, secondInput), 28);
    }

    public static int solution(List<Integer> firstInput, List<Integer> secondInput){
        int answer = 0;
        final int N = firstInput.get(0);
        final int M = firstInput.get(1);
        final int K = firstInput.get(2);

        Collections.sort(secondInput, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 < o2 ? 1 : -1;
            }
        });

        int i = 0, j = 0;
        for(int count = 0; count < M; ++count){
            answer += secondInput.get(i);
            j++;
            if(j == K){
                if(secondInput.get(i + 1) < secondInput.get(i)){
                    answer += secondInput.get(i + 1);
                    count++;
                }
                j = 0;
            }
        }
        return answer;
    }
}
