package dp;

import java.util.Scanner;
import java.util.stream.IntStream;

public class 금광 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int testCase = 1; testCase <= t; ++testCase){

            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] arr = new int[n][m];
            int[][] dp = new int[n][m];
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    arr[i][j] = sc.nextInt();
                }
            }

            for(int i = 0; i < n; ++i){
                dp[i][0] = arr[i][0];
            }

            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    if(i - 1 >= 0 && j - 1 >= 0){
                        dp[i][j] = Math.max(dp[i - 1][j - 1] + arr[i][j], dp[i][j]);
                    }
                    if(j - 1 >= 0){
                        dp[i][j] = Math.max(dp[i][j - 1] + arr[i][j], dp[i][j]);
                    }
                    if(i + 1 < n && j - 1 >= 0){
                        dp[i][j] = Math.max(dp[i + 1][j - 1] + arr[i][j], dp[i][j]);
                    }
                }
            }

            int max = 0;
            for(int i = 0; i < n; ++i){
                if(dp[i][m - 1] > max) max = dp[i][m - 1];
            }
            System.out.println(max);

        }
    }
}
