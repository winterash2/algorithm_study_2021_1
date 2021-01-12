package greedy;

import org.junit.Test;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class Juneui_곱하기혹은더하기 {

    @Test
    public static void main(String[] args){
        String input = "02984";
        assertThat(solution(input), equalTo(576));
        input = "567";
        assertThat(solution(input), equalTo(210));
        input = "123";
        assertThat(solution(input), equalTo(9));
        input = "01234";
        assertThat(solution(input), equalTo(36));
        input = "12034";
        assertThat(solution(input), equalTo(36));
        input = "0";
        assertThat(solution(input), equalTo(0));
        input = "1";
        assertThat(solution(input), equalTo(1));
        input = "012012";
        assertThat(solution(input), equalTo(8));
    }

    public static int solution(String input){
        int answer = 0;
        for(int i = 0; i < input.length(); ++i){
            int value = input.charAt(i) - '0';
            answer = Math.max(answer + value, answer * value);
        }
        return answer;
    }
}
