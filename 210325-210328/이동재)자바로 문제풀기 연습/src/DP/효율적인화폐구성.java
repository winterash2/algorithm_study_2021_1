package DP;

import java.util.Scanner;

public class 효율적인화폐구성 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int inf = 1000000000;
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] coins = new int[N];
        for(int i = 0; i < N; i++){
            coins[i] = sc.nextInt();
        }
        int[] dp = new int[M + 1];
        for(int i = 0; i < M+1; i++){
            dp[i] = inf;
        }
        dp[0] = 0;
        for (int c = 0; c < N; c++) {
            int coin = coins[c];
            for(int i = coin; i < M+1; i++){
                if(dp[i-coin] != inf){
                    dp[i] = Integer.min(dp[i], dp[i-coin]+1);
                }
            }
//            for(int i=0; i<M+1; i++){
//                System.out.print(dp[i] + " ");
//            }
//            System.out.println();
        }

        int answer = dp[M];
        if (answer == inf){
            answer = -1;
        }
        System.out.println(answer);
    }
}
/*
2 15
2
3
 */