package greedy;

import static org.hamcrest.core.IsEqual.equalTo;
import static org.junit.Assert.assertThat;

public class Juneui_문자열뒤집기 {
    public static void main(String[] args) {
        String input = "0001100";
        assertThat(solution(input), equalTo(1));
    }

    public static int solution(String input) {
        int answer = 0;

        int zeroCount = 0;
        int oneCount = 0;
        for (int i = 0; i < input.length() - 1; ++i) {
            int value = input.charAt(i) - '0';
            int nextValue = input.charAt(i + 1) - '0';
            if (value == 0 && value != nextValue) {
                zeroCount++;
            } else if (value == 1 && value != nextValue) {
                oneCount++;
            }
        }
        if (input.charAt(input.length() - 1) - '0' == 0) {
            zeroCount++;
        } else {
            oneCount++;
        }
        answer = Math.min(zeroCount, oneCount);

        return answer;
    }
}
