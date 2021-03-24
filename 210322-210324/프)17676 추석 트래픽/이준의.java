/*
정확성  테스트
테스트 1 〉	통과 (1.18ms, 53.2MB)
테스트 2 〉	통과 (12.58ms, 54.8MB)
테스트 3 〉	실패 (31.79ms, 56.1MB)
테스트 4 〉	통과 (1.02ms, 52MB)
테스트 5 〉	통과 (2.08ms, 52.7MB)
테스트 6 〉	통과 (2.42ms, 52.5MB)
테스트 7 〉	통과 (14.25ms, 55MB)
테스트 8 〉	통과 (12.78ms, 54.7MB)
테스트 9 〉	통과 (2.23ms, 52.7MB)
테스트 10 〉	통과 (0.84ms, 53.4MB)
테스트 11 〉	통과 (1.46ms, 52.3MB)
테스트 12 〉	통과 (16.03ms, 55.5MB)
테스트 13 〉	통과 (2.69ms, 52.5MB)
테스트 14 〉	통과 (0.74ms, 52.7MB)
테스트 15 〉	실패 (0.73ms, 52.5MB)
테스트 16 〉	통과 (0.68ms, 52.4MB)
테스트 17 〉	통과 (0.72ms, 53.3MB)
테스트 18 〉	실패 (21.24ms, 56.3MB)
테스트 19 〉	통과 (26.82ms, 56.4MB)
테스트 20 〉	통과 (27.50ms, 56.4MB)
테스트 21 〉	통과 (0.02ms, 52.5MB)
테스트 22 〉	통과 (0.02ms, 53MB)
 */

import java.util.*;
import java.io.*;

class Traffic{
    int start, end;
    public Traffic(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

class Solution {
    public int solution(String[] lines) {
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

        int left = 0, right = 1;
        int cnt = 1;
        int slideStart = traffic[0].start;
        int slideEnd = traffic[0].start + 1000;
        while(left < len && right < len){
            if((traffic[right].start < slideStart && traffic[right].end < slideStart) || (traffic[right].start > slideEnd && traffic[right].end > slideEnd)){
                cnt--;
                left++;
                if(right != len){
                    slideStart = traffic[left].start;
                    slideEnd = slideStart + 1000;
                }
            } else {
                cnt++;
                if(cnt > answer) answer = cnt;
                right++;
            }
        }

        left = 0;
        right = 1;
        cnt = 1;
        slideStart = traffic[0].end;
        slideEnd = traffic[0].end + 1000;
        while(left < len && right < len){
            if((traffic[right].start < slideStart && traffic[right].end < slideStart) || (traffic[right].start > slideEnd && traffic[right].end > slideEnd)){
                cnt--;
                left++;
                if(right != len){
                    slideStart = traffic[left].end;
                    slideEnd = slideStart + 1000;
                }
            } else {
                cnt++;
                if(cnt > answer) answer = cnt;
                right++;
            }
        }
        return answer;
    }
}