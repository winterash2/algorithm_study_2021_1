package binarysearch;

public class 가사검색 {
    public static void main(String[] args) {
        String[] words = new String[]{"frodo", "front", "frost", "frozen", "frame", "kakao"};
        String[] quires = new String[]{"fro??", "????o", "fr???", "fro???", "pro?"};
        solution(words, quires);
    }

    public static boolean check(String word, String query){
        for(int i = 0; i < query.length(); ++i){
            if(query.charAt(i) != '?' && query.charAt(i) != word.charAt(i)) {
                return false;
            }
        }
        return true;
    }

    public static int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];

        int count = 0;
        for(int i = 0; i < queries.length; ++i){
            for(int j = 0; j < words.length; ++j){
                if(words[j].length() != queries[i].length()) continue;
                if(check(words[j], queries[i])) count++;
            }
            answer[i] = count;
            count = 0;
        }
        return answer;
    }
}


/*
채점을 시작합니다.
정확성  테스트
테스트 1 〉	통과 (0.28ms, 52.9MB)
테스트 2 〉	통과 (0.17ms, 52.2MB)
테스트 3 〉	통과 (0.20ms, 52.2MB)
테스트 4 〉	통과 (0.18ms, 52.3MB)
테스트 5 〉	통과 (0.11ms, 52.6MB)
테스트 6 〉	통과 (0.17ms, 51.9MB)
테스트 7 〉	통과 (8.48ms, 53MB)
테스트 8 〉	통과 (9.75ms, 52.1MB)
테스트 9 〉	통과 (7.54ms, 53MB)
테스트 10 〉	통과 (5.93ms, 54.5MB)
테스트 11 〉	통과 (5.79ms, 52.3MB)
테스트 12 〉	통과 (10.12ms, 52.8MB)
테스트 13 〉	통과 (35.43ms, 53.6MB)
테스트 14 〉	통과 (32.62ms, 54MB)
테스트 15 〉	통과 (37.86ms, 53.6MB)
테스트 16 〉	통과 (33.28ms, 55MB)
테스트 17 〉	통과 (31.07ms, 56MB)
테스트 18 〉	통과 (26.98ms, 54MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (22.78ms, 59.8MB)
테스트 5 〉	통과 (28.59ms, 59.7MB)
채점 결과
정확성: 25.0
효율성: 30.0
합계: 55.0 / 100.0
 */



package binarysearch;

public class 가사검색2 {
    public static void main(String[] args) {
        String[] words = new String[]{"frodo", "front", "frost", "frozen", "frame", "kakao"};
        String[] quires = new String[]{"fro??", "????o", "fr???", "fro???", "pro?"};
        solution(words, quires);
    }

    public static int findLeftIndex(String query){
        int left = 0;
        int right = query.length();
        int index = 0;
        while(left <= right){
            int mid = (int) (left + right) / 2;
            if(query.charAt(mid) == '?' && query.charAt(mid - 1) != '?'){
                index = mid;
                break;
            } else if(query.charAt(mid) != '?'){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return index;
    }

    public static int findRightIndex(String query){
        int left = 0;
        int right = query.length();
        int index = 0;
        while(left <= right){
            int mid = (int) (left + right) / 2;
            if(query.charAt(mid) == '?' && query.charAt(mid + 1) != '?'){
                index = mid;
                break;
            } else if(query.charAt(mid) != '?'){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return index;
    }

    public static int[] solution(String[] words, String[] queries) {
        int[] answer = new int[queries.length];

        int count = 0;
        for(int i = 0; i < queries.length; ++i){
            for(int j = 0; j < words.length; ++j){
                if(words[j].length() != queries[i].length()) continue;
                int leftIndex = 0;
                int rightIndex = 0;
                if(queries[i].charAt(0) == '?' && queries[i].charAt(queries[i].length() - 1) == '?'){
                    count++;
                    continue;
                } else if (queries[i].charAt(0) == '?') {
                    rightIndex = findRightIndex(queries[i]);
                    System.out.println("rightIndex : " + rightIndex + " " + queries[i]);
                    boolean check = true;
                    for(int k = rightIndex + 1; k < words[j].length(); ++k) {
                        if(words[j].charAt(k) != queries[i].charAt(k)) {
                            check = false;
                            break;
                        }
                    }
                    if(check) count++;
                } else {
                    leftIndex = findLeftIndex(queries[i]);
                    System.out.println("leftIndex : " + leftIndex  + " " + queries[i]);
                    boolean check = true;
                    for(int k = leftIndex - 1; k >= 0; --k) {
                        if(words[j].charAt(k) != queries[i].charAt(k)) {
                            check = false;
                            break;
                        }
                    }
                    if(check) count++;
                }
            }
            answer[i] = count;
            count = 0;
        }
        return answer;
    }
}

/*
정확성  테스트
테스트 1 〉	통과 (0.19ms, 52.9MB)
테스트 2 〉	통과 (0.22ms, 52.6MB)
테스트 3 〉	통과 (0.22ms, 52.1MB)
테스트 4 〉	통과 (0.21ms, 53MB)
테스트 5 〉	통과 (0.22ms, 52.6MB)
테스트 6 〉	통과 (0.20ms, 52.7MB)
테스트 7 〉	통과 (9.02ms, 54.9MB)
테스트 8 〉	통과 (8.80ms, 52.8MB)
테스트 9 〉	통과 (12.41ms, 52.6MB)
테스트 10 〉	통과 (7.04ms, 52.2MB)
테스트 11 〉	통과 (6.36ms, 52.9MB)
테스트 12 〉	통과 (10.45ms, 52.9MB)
테스트 13 〉	통과 (40.97ms, 54.2MB)
테스트 14 〉	통과 (45.06ms, 53.7MB)
테스트 15 〉	통과 (74.03ms, 56MB)
테스트 16 〉	통과 (46.40ms, 54MB)
테스트 17 〉	통과 (50.60ms, 54.9MB)
테스트 18 〉	통과 (48.85ms, 54.1MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (56.30ms, 61.2MB)
테스트 5 〉	통과 (31.61ms, 61.4MB)
채점 결과
정확성: 25.0
효율성: 30.0
합계: 55.0 / 100.0
 */