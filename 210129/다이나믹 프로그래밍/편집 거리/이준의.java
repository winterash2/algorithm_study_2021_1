package dp;

import java.util.Scanner;

public class 편집거리 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str1 = sc.nextLine();
        String str2 = sc.nextLine();
        int n = str1.length();
        int m = str2.length();

        int[][] dp = new int[n + 1][m + 1];

        for(int i = 1; i <= n; ++i){
            dp[i][0] = i;
        }
        for(int j = 1; j <= m; ++j){
            dp[0][j] = j;
        }

        
        for(int i = 1; i < n + 1; ++i){
            for(int j = 1; j < m + 1; ++j){
                if(str1.charAt(i - 1) == str2.charAt(j - 1)){
                    dp[i][j] = dp[i - 1][j - 1];
                }else{
                    dp[i][j] = 1 + Math.min(Math.min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]);
                }
            }
        }

        System.out.println(dp[n][m]);
    }
}

// https://hsp1116.tistory.com/41    <- Levenstein 알고리즘을 가장 잘 설명한듯!