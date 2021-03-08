//class Solution {
//
//    static int[][] puddle;
//    static int M, N, cnt;
//
//    static void findPathCount(int m, int n){
//        if(m > M || n > N) return;
//        if(m == M && n == N){
//            cnt++;
//            cnt %= 1000000007;
//            return;
//        }
//        for(int i = 0; i < puddle.length; ++i){
//            if(m == puddle[i][1] && n == puddle[i][0]) return;
//        }
//
//        findPathCount(m + 1, n);
//        findPathCount(m, n + 1);
//    }
//
//    public int solution(int m, int n, int[][] puddles) {
//        int answer = 0;
//        puddle = puddles;
//        M = m;
//        N = n;
//        findPathCount(1, 1);
//        return cnt;
//    }
//}


class Solution {
    public long solution(int m, int n, int[][] puddles) {
        long[][] root = new long[101][101];
        long[][] puddle = new long[101][101];

        for(int[] p : puddles) {
            if(puddle.length == 0) break;
            puddle[p[0]][p[1]] = -1;
        }

        root[0][1] = 1;
        for(int i = 1; i <= m; ++i){
            for(int j = 1; j <= n; ++j){
                if(puddle[i][j] == -1){
                    root[i][j] = 0;
                } else {
                    root[i][j] = (root[i][j - 1] + root[i-1][j]) % 1000000007;
                }
            }
        }
        return root[m][n];
    }
}