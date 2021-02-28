package dp;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class rgb거리 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][N];
        for(int i = 0; i < N; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; ++j){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int[][] dp = new int[2][3];
        for(int i = 0; i < 3; ++i){
            dp[0][i] = arr[0][i];
        }

        int preIndex = 0, curIndex = 1;
        for(int i = 1; i < N; ++i){
            dp[curIndex][0] = arr[i][0] + Math.min(dp[preIndex][1], dp[preIndex][2]);
            dp[curIndex][1] = arr[i][1] + Math.min(dp[preIndex][0], dp[preIndex][2]);
            dp[curIndex][2] = arr[i][2] + Math.min(dp[preIndex][0], dp[preIndex][1]);
            preIndex = (1 - preIndex) % 2;
            curIndex = (1 - curIndex) % 2;
        }
        int answer = Integer.MAX_VALUE;
        for(int i = 0; i < 3; ++i){
            if(dp[preIndex][i] < answer) answer = dp[preIndex][i];
        }
        System.out.println(answer);
    }
}

/*
3
26 40 83
49 60 57
13 89 99
 */
