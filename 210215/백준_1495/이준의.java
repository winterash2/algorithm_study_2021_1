package dp;

import java.util.Scanner;

public class 기타리스트 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int m = sc.nextInt();
        int[] v = new int[n + 1];
        for(int i = 1; i < n + 1; ++i){
            v[i] = sc.nextInt();
        }

        boolean[][] dp = new boolean[n + 1][m + 1];

        dp[0][s] = true;

        for(int i = 1; i < n + 1; ++i){
            for(int j = 0; j <= m; ++j){
                if(!dp[i - 1][j]) continue;
                if(j - v[i] >= 0){
                    dp[i][j - v[i]] = true;
                }
                if(j + v[i] <= m){
                    dp[i][j + v[i]] = true;
                }
            }
        }

        boolean check = false;
        for(int i = m; i >= 0; --i){
            if(dp[n][i]){
                check = true;
                System.out.println(i);
                break;
            }
        }
        if(!check){
            System.out.println("-1");
        }
    }
}

/*
3 5 10
5 3 7
 */