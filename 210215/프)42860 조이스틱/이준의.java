class Solution {
    public int solution(String name) {
        int answer = 0;
        String tmp = "";
        int index = 0;
        for(int i = 0; i < name.length(); ++i) tmp += "A";
        while(true){
            int left = 1;
            int right = 1;

            answer += Math.min(name.charAt(index) - 'A', 'Z' - name.charAt(index) + 1);
            name = name.substring(0, index) + 'A' + name.substring(index + 1);

            if(name.equals(tmp)) break;

            for(int i = 1; index + i < name.length(); ++i){
                if(name.charAt(index + i) == 'A') right += 1;
                else break;
            }
            for(int i = 1; i < name.length() - 1; ++i) {
                int minusIndex = index - i < 0 ? name.length() + index - i : index - i;
                if(name.charAt(minusIndex) == 'A') left += 1;
                else break;
            }

            if(right > left){
                answer += left;
                index = index - left < 0 ? name.length() + index - left : index - left;
            } else {
                answer += right;
                index += right;
            }
        }
        return answer;
    }
}
/*
런타임 에러 나는데 다시 봐야할
 */
/*
정확성  테스트
테스트 1 〉	통과 (11.82ms, 53.2MB)
테스트 2 〉	통과 (12.89ms, 52.8MB)
테스트 3 〉	통과 (14.33ms, 53.4MB)
테스트 4 〉	실패 (런타임 에러)
테스트 5 〉	통과 (12.88ms, 53.3MB)
테스트 6 〉	통과 (12.42ms, 53.3MB)
테스트 7 〉	실패 (런타임 에러)
테스트 8 〉	실패 (런타임 에러)
테스트 9 〉	통과 (12.33ms, 53.6MB)
테스트 10 〉	통과 (13.16ms, 52.6MB)
테스트 11 〉	실패 (런타임 에러)
채점 결과
정확성: 63.6
합계: 63.6 / 100.0
 */