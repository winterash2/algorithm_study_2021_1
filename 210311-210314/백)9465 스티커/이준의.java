package dp;

import java.util.*;
import java.io.*;

public class 스티커 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());

        for(int testCase = 0; testCase < t; ++testCase){
            int n = Integer.parseInt(br.readLine());
            int[][] sticker = new int[2][n];

            for(int i = 0; i < 2; ++i){
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < n; ++j){
                    sticker[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            int[][] dp = new int[2][n];
            dp[0][0] = sticker[0][0];
            dp[1][0] = sticker[1][0];

            if(n > 1){
                dp[0][1] = dp[1][0] + sticker[0][1];
                dp[1][1] = dp[0][0] + sticker[1][1];

                for(int i = 2; i < n; ++i){
                    dp[0][i] = Math.max(dp[1][i - 2] + sticker[0][i], dp[1][i - 1] + sticker[0][i]);
                    dp[1][i] = Math.max(dp[0][i - 2] + sticker[1][i], dp[0][i - 1] + sticker[1][i]);
                }

            }
            bw.write(Math.max(dp[0][n - 1], dp[1][n - 1]) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
/*
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
 */

