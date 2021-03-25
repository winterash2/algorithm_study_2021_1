/*
정확성  테스트
테스트 1 〉	통과 (3.39ms, 53MB)
테스트 2 〉	통과 (13.11ms, 55.4MB)
테스트 3 〉	실패 (16.16ms, 54.9MB)
테스트 4 〉	통과 (1.72ms, 53MB)
테스트 5 〉	통과 (3.05ms, 52.4MB)
테스트 6 〉	통과 (3.07ms, 53.1MB)
테스트 7 〉	통과 (17.24ms, 55.6MB)
테스트 8 〉	통과 (14.11ms, 55.8MB)
테스트 9 〉	통과 (2.85ms, 52.7MB)
테스트 10 〉	통과 (1.68ms, 52.9MB)
테스트 11 〉	통과 (2.36ms, 52.7MB)
테스트 12 〉	통과 (14.89ms, 55.7MB)
테스트 13 〉	통과 (3.17ms, 53MB)
테스트 14 〉	통과 (1.81ms, 53.2MB)
테스트 15 〉	통과 (1.56ms, 52.8MB)
테스트 16 〉	통과 (1.91ms, 52.8MB)
테스트 17 〉	통과 (2.00ms, 53.3MB)
테스트 18 〉	실패 (34.50ms, 56.2MB)
테스트 19 〉	통과 (23.69ms, 56MB)
테스트 20 〉	통과 (27.58ms, 55.4MB)
테스트 21 〉	통과 (0.02ms, 52.1MB)
테스트 22 〉	통과 (0.02ms, 52.3MB)
채점 결과
정확성: 90.9
합계: 90.9 / 100.0

3, 18 번 모르겠다ㅠ
 */

package simulation;

import soma.B;

import java.math.BigDecimal;
import java.util.*;
import java.io.*;

class Traffic{
    int start, end;
    public Traffic(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class 추석트래픽 {

    public static int solution(String[] lines){
        int answer = 0;
        if(lines.length == 1) return 1;
        int len = lines.length;
        StringTokenizer st;
        Traffic[] traffic = new Traffic[len];
        for(int i = 0; i < len; ++i){
            st = new StringTokenizer(lines[i]);
            st.nextToken();
            String S = st.nextToken();
            String T = st.nextToken();
            int time = Integer.parseInt(S.substring(0, 2)) * 3600 * 1000 + Integer.parseInt(S.substring(3, 5)) * 60 * 1000 + (int)(Double.parseDouble(S.substring(6, S.length())) * 1000);
            int t = (int)(Double.parseDouble(T.substring(0, T.length() - 1)) * 1000);
            traffic[i] = new Traffic(time - t + 1, time);
        }
        Arrays.sort(traffic, (a, b) -> {
            return a.start - b.start;
        });
        int left = 0, right = 1;
        int cnt = 1;
        int slideStart = traffic[0].start;
        int slideEnd = traffic[0].start + 1000 - 1;
        while(left < len && right < len){
            if((traffic[right].start < slideStart && traffic[right].end < slideStart) || (traffic[right].start > slideEnd && traffic[right].end > slideEnd)){
                cnt--;
                left++;
                if(left != len){
                    slideStart = traffic[left].start;
                    slideEnd = slideStart + 1000 - 1;
                }
            } else {
                cnt++;
                if(cnt > answer) answer = cnt;
                right++;
            }
        }

        Arrays.sort(traffic, (a, b) -> {
            return a.end - b.end;
        });
        left = 0;
        right = 1;
        cnt = 1;
        slideStart = traffic[0].end;
        slideEnd = traffic[0].end + 1000 - 1;
        while(left < len && right < len){
            if((traffic[right].start < slideStart && traffic[right].end < slideStart) || (traffic[right].start > slideEnd && traffic[right].end > slideEnd)){
                cnt--;
                left++;
                if(left != len){
                    slideStart = traffic[left].end;
                    slideEnd = slideStart + 1000 - 1;
                }
            } else {
                cnt++;
                if(cnt > answer) answer = cnt;
                right++;
            }
        }
        return answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] input = new String[]{"2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"};
        bw.write(solution(input) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

