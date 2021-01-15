package simulation;

import java.util.ArrayList;
import java.util.Arrays;

import static org.junit.Assert.assertEquals;

public class 문자열재정렬 {
    public static void main(String[] args){
        assertEquals(solution("K1KA5CB7"), "ABCKK13");
        assertEquals(solution("AJKDLSI412K4JSJ9D"), "ADDIJJJKKLSS20");
    }
    public static String solution(String input){
        String answer = "";

        String alpha = "";
        int sum = 0;
        for(int i = 0; i < input.length(); ++i){
            if(Character.isDigit(input.charAt(i))){
                sum += input.charAt(i) - '0';
            } else {
                alpha += input.charAt(i);
            }
        }
        char[] sorted = alpha.toCharArray();
        Arrays.sort(sorted);
        return String.valueOf(sorted)+String.valueOf(sum);
    }
}
