package dp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class LCS {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        char[] a = br.readLine().toCharArray();
        char[] b = br.readLine().toCharArray();
        int[][] dp = new int[a.length + 1][b.length + 1];

        for(int i = 1; i <= a.length; ++i){
            for(int j = 1; j <= b.length; ++j)
            {
                if(a[i - 1] == b[j - 1]){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }

        bw.write(dp[a.length][b.length] + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}
/*
ACAYKP
CAPCAK
 */