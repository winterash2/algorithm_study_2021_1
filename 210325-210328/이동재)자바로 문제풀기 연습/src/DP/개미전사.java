import java.util.Scanner;

public class 개미전사 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] soldiers = new int[N];
        int[] dp = new int[N];
        for(int i = 0; i < N; i++){
            soldiers[i] = sc.nextInt();
            dp[i] = 0;
        }
        dp[0] = soldiers[0];
        dp[1] = Integer.max(dp[0], soldiers[1]);
        for(int i=2; i<N; i++){
            dp[i] = Integer.max(dp[i-1], dp[i-2]+soldiers[i]);
        }
        int answer = dp[N - 1];
        System.out.println(answer);
    }
}
/*
4
1 3 1 5
 */