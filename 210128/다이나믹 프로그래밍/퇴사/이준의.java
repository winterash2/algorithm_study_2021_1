package dp;

import java.util.Scanner;

public class 퇴사 {
    public static void main(String[] args) {
        int[] d = new int[1000];
        int[] t = new int[1000];
        int[] p = new int[1000];

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i = 1; i <= n; ++i){
            t[i] = sc.nextInt();
            p[i] = sc.nextInt();
        }

        int next = 0;
        for(int j = n; j > 0; --j){
            next = j + t[j];
            if(next > n + 1){
                d[j] = d[j + 1];
            } else {
                d[j] = Math.max(d[j + 1], d[next] + p[j]);
            }
        }

        System.out.println(d[1]);
    }
}
