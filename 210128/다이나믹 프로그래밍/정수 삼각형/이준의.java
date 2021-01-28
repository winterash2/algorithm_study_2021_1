package dp;

import java.util.Scanner;
import java.util.stream.IntStream;

public class 정수삼각형 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] arr = new int[n][n];

        for(int i = 0; i < n; ++i){
            for(int j = 0; j <= i; ++j){
                arr[i][j] = sc.nextInt();
            }
        }

        int[][] d = new int[n][n];
        d[0][0] = arr[0][0];
        for(int i = 1; i < n; ++i){
            for(int j = 0; j <= i; ++j){
                if(j - 1 >= 0) d[i][j] = Math.max(d[i - 1][j] + arr[i][j], d[i - 1][j - 1] + arr[i][j]);
                else d[i][j] = d[i-1][j] + arr[i][j];
            }
        }

        int max = IntStream.of(d[n - 1]).max().getAsInt();
        System.out.println(max);
    }
}
