package simulation;

import static org.junit.Assert.assertEquals;

public class 왕실의나이트 {
    public static void main(String[] args){
        String input = "a1";
        assertEquals(solution(input), 2);
    }
    public static int solution(String input){
        int answer = 0;
        int[] start = {0, 0};
        start[0] = input.charAt(0) - 'a' + 1;
        start[1] = input.charAt(1) - '0';

        int[] dx = {-1, -2, -2, -1, 1, 2, 2, 1};
        int[] dy = {2, 1, -1, -2, -2, -1, 1, 2};

        for(int i = 0; i < 8; ++i){
            int[] cur = start.clone();
            cur[0] += dx[i];
            cur[1] += dy[i];
            if(cur[0] < 1 || cur[1] > 8 || cur[1] < 1 || cur[1] > 8) continue;
            answer++;
        }

        return answer;
    }
}
