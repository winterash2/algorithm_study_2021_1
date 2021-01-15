package simulation;

import static org.junit.Assert.assertArrayEquals;

public class 상하좌우 {
    public static void main(String[] args){
        int N = 5;
        String input = "RRRUDD";
        int[] answer = {3, 4};
        assertArrayEquals(solution(N, input), answer);
    }


    public static int[] solution(int N, String input){
        int[] answer = new int[]{};
        int[] start = {1, 1};
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};

        for(int i = 0; i < input.length(); ++i){
            int[] next = start.clone();
            if(input.charAt(i) == 'R') {
                next[0] += dx[2];
                next[1] += dy[2];
            } else if (input.charAt(i) == 'L'){
                next[0] += dx[3];
                next[1] += dy[3];
            } else if (input.charAt(i) == 'U') {
                next[0] += dx[1];
                next[1] += dy[1];
            } else {
                next[0] += dx[0];
                next[1] += dy[0];
            }
            if(next[0] < 1 || next[0] > input.length() || next[1] < 1 || next[1] > input.length()) continue;
            start = next;
        }
        answer = start;
        return answer;
    }
}
