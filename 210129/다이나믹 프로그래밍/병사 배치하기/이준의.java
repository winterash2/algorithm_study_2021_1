package dp;

import java.util.Scanner;
import java.util.stream.IntStream;

public class 병사배치하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n + 1];
        for(int i = 0; i < n; ++i){
            arr[i] = sc.nextInt();
        }

        int[] dp = new int[n + 1];

        for(int i = 0; i < n; ++i){
            dp[i] = 1;
        }
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < i; ++j){
                if(arr[j] > arr[i]){
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        int max = IntStream.of(dp).max().getAsInt();
        System.out.println(n - max);
    }
}
