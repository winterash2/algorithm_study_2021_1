package simulation;

import static org.junit.Assert.assertEquals;

public class 럭키스트레이트 {
    public static void main(String[] args){
        assertEquals(solution(123402), "LUCKY");
        assertEquals(solution(7755), "READY");
    }
    public static String solution(int n){
        String answer = "";
        String value = String.valueOf(n);
        int i;
        int sum1 = 0;
        int sum2 = 0;
        for(i = 0; i < value.length() / 2; ++i){
            sum1 += value.charAt(i);
        }
        for(int j = i; j < value.length(); ++j){
            sum2 += value.charAt(j);
        }
        return sum1 == sum2 ? "LUCKY" : "READY";
    }
}
