package greedy;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Juneui_1이될때까지 {
    @Test
    public static void main(String[] args){
        assertEquals(solution(25, 5), 2);
        assertEquals(solution(17, 4 ), 3);
    }

    public static int solution(int n, int k){
        int answer = 0;
        while(n > 1){
            n = n % k == 0 ? n / k : n - 1;
            answer++;
        }
        return answer;
    }
}
