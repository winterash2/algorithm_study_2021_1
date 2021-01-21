package dfsbfs;

import java.util.Stack;

import static org.junit.Assert.assertEquals;

public class 괄호변환 {
    public static void main(String[] args) {
        assertEquals(solution("(()())()"), "(()())()");
        assertEquals(solution(")("), "()");
        assertEquals(solution("()))((()"), "()(())()");
    }

    public static int balencedString(String s){
        int count = 0;
        for(int i = 0 ; i < s.length(); ++i){
            if(s.charAt(i) == '(') count++;
            else count--;
            if(count == 0) return i;
        }
        return -1;
    }

    public static boolean check(String s){
        Stack<Character> st = new Stack<>();
        for(char ch : s.toCharArray()){
            if(ch == '('){
                st.push(ch);
            } else {
                if(st.isEmpty() || st.peek() == ')'){
                    return false;
                }
                st.pop();
            }
        }
        return true;
    }

    public static String solution(String input){
        if(input.equals(""))
            return input;

        int index = balencedString(input);
        String u = input.substring(0, index + 1), v = input.substring(index + 1);
        if(check(u)){
            return u + solution(v);
        } else {
            String newU = "";
            u = u.substring(1, u.length()-1);
            for(char ch : u.toCharArray()){
                if(ch == '(')
                    newU += ')';
                else
                    newU += '(';
            }
            return '(' + solution(v) + ')' + newU;
        }
    }
}
