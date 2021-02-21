package dp;

import java.util.Scanner;

public class 동전1 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] d = new int[n];
        for(int i = 0; i < n; ++i){
            d[i] = sc.nextInt();
        }
        int[] dp = new int[k + 1];
        dp[0] = 1;
        for(int i = 0; i < n; ++i){
            for(int j = d[i]; j <= k; ++j){
                if(j - d[i] >= 0) dp[j] += dp[j - d[i]];
            }
        }
        System.out.println(dp[k]);
    }
}
/*
3 10
1 2 5
 */
