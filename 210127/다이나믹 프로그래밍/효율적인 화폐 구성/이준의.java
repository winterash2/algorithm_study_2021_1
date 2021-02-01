package dp;

import java.util.Scanner;

public class 효율적인화폐구성 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] dp = new int[10001];
        int[] coins = new int[n];
        for(int i = 0; i < n; ++i){
            coins[i] = sc.nextInt();
        }
        for(int i = 1; i <= 10000; ++i){
            dp[i] = 10001;
        }

        for(int i = 0; i < n; ++i){
            for(int j = 1; j <= m; ++j){
                if(j - coins[i] >= 0 && dp[j - coins[i]] != 10001){
                    dp[j] = Math.min(dp[j], dp[j - coins[i]] + 1);
                }
            }
        }

        if(dp[m] == 10001){
            System.out.println("-1");
        }else{
            System.out.println(dp[m]);
        }
    }
}
