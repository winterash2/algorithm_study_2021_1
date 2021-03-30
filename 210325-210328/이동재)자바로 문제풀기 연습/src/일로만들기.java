import java.util.Scanner;

public class 일로만들기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        final int inf = 1000000000;
        int N = sc.nextInt();
        int[] dp = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            dp[i] = inf;
        }
        dp[1] = 1;
        for (int i = 1; i < N + 1; i++) {
            if (dp[i] != inf & i * 5 <= N) {
                dp[i * 5] = Integer.min(dp[i * 5], dp[i] + 1);
            }
            if (dp[i] != inf & i * 3 <= N) {
                dp[i * 3] = Integer.min(dp[i * 3], dp[i] + 1);
            }
            if (dp[i] != inf & i * 2 <= N) {
                dp[i * 2] = Integer.min(dp[i * 2], dp[i] + 1);
            }
            if (dp[i] != inf & i + 1 <= N) {
                dp[i + 1] = Integer.min(dp[i + 1], dp[i] + 1);
            }
        }
//        for (int i = 1; i < N + 1; i++) {
//            System.out.print(dp[i] + " ");
//        }
        System.out.println(dp[N] - 1);
    }
}
