package simulation;

import static org.junit.Assert.assertEquals;

public class 문자열압축 {
    public static void main(String[] args){
        assertEquals(solution("aabbaccc"), 7);
        assertEquals(solution("ababcdcdababcdcd"), 9);
        assertEquals(solution("abcabcdede"), 8);
        assertEquals(solution("abcabcabcabcdededededede"), 14);
        assertEquals(solution("xababcdcdababcdcd"), 17);
    }
    public static int solution(String input){
        int answer = input.length();

        for(int i = 1; i < input.length() / 2 + 1; ++i){
            String newStr = "";
            int count = 1;
            String sub = input.substring(0, i);
            for(int j = i; j < input.length(); j += i){
                int start = j;
                int end = j + i > input.length() ? input.length() : j + i;
                if(input.substring(start, end).equals(sub)){
                    count++;
                }else{
                    newStr += count >= 2 ? count + sub : sub;
                    count = 1;
                    sub = input.substring(start, end);
                }
            }
            newStr += count >= 2 ? count + sub : sub;
            answer = answer > newStr.length() ? newStr.length() : answer;
        }
        return answer;
    }
}
