import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;

        Arrays.sort(people);

        int left = 0;
        int right = people.length - 1;
        while(left < right){
            if(people[left] + people[right] <= limit){
                answer++;
                left++;
                right--;
            } else {
                right--;
                answer++;
            }
        }
        if(left == right) answer++;
        return answer;
    }
}
/*
정확성  테스트
테스트 1 〉	통과 (2.10ms, 52.9MB)
테스트 2 〉	통과 (1.07ms, 52.3MB)
테스트 3 〉	통과 (1.82ms, 53.1MB)
테스트 4 〉	통과 (1.85ms, 52.7MB)
테스트 5 〉	통과 (1.29ms, 53.8MB)
테스트 6 〉	통과 (0.93ms, 53.3MB)
테스트 7 〉	통과 (0.88ms, 52.4MB)
테스트 8 〉	통과 (0.46ms, 53.4MB)
테스트 9 〉	통과 (0.55ms, 53MB)
테스트 10 〉	통과 (1.54ms, 52.4MB)
테스트 11 〉	통과 (1.84ms, 52.3MB)
테스트 12 〉	통과 (1.48ms, 53.1MB)
테스트 13 〉	통과 (1.07ms, 52.7MB)
테스트 14 〉	통과 (0.94ms, 52.8MB)
테스트 15 〉	통과 (0.60ms, 52.6MB)
효율성  테스트
테스트 1 〉	통과 (10.07ms, 54MB)
테스트 2 〉	통과 (9.95ms, 54.9MB)
테스트 3 〉	통과 (11.31ms, 54.5MB)
테스트 4 〉	통과 (6.83ms, 53.8MB)
테스트 5 〉	통과 (9.37ms, 54.5MB)
채점 결과
정확성: 75.0
효율성: 25.0
합계: 100.0 / 100.0
 */