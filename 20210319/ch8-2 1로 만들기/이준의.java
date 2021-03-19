package dp;

import java.util.*;
import java.io.*;

public class 복습_1로만들기 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int x = Integer.parseInt(br.readLine());
        int[] dp = new int[x + 1];
        for(int i = 0; i <= x; ++i) dp[i] = Integer.MAX_VALUE;
        dp[0] = 0;
        dp[1] = 0;
        for(int i = 1; i <= x; ++i){
            if(i - 1 >= 0){
                dp[i] = Math.min(dp[i], dp[i - 1] + 1);
            }
            if(i % 2 == 0){
                dp[i] = Math.min(dp[i], dp[i / 2] + 1);
            }
            if(i % 3 == 0){
                dp[i] = Math.min(dp[i], dp[i / 3] + 1);
            }
            if(i % 5 == 0){
                dp[i] = Math.min(dp[i], dp[i / 5] + 1);
            }
        }
        bw.write(dp[x] + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
26
 */



//package dp;
//
//import java.util.*;
//import java.io.*;
//
//public class 복습_1로만들기 {
//
//    static int recursion(int x){
//        if(x == 1){
//            return 0;
//        }
//        int a = Integer.MAX_VALUE, b = Integer.MAX_VALUE, c = Integer.MAX_VALUE, d = Integer.MAX_VALUE;
//        if(x % 5 == 0){
//            a = recursion(x / 5);
//        }
//        if(x % 3 == 0){
//            b = recursion(x / 3);
//        }
//        if(x % 3 == 0){
//            c = recursion(x / 2);
//        }
//        d = recursion(x - 1);
//        return 1 + Math.min(Math.min(a, b), Math.min(c, d));
//    }
//
//    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        int x = Integer.parseInt(br.readLine());
//        bw.write(recursion(x) + "\n");
//        bw.flush();
//        bw.close();
//        br.close();
//    }
//}

// 메모
/*
package dp;

import java.util.*;
import java.io.*;

public class 복습_1로만들기 {

    static int[] cache;

    static int recursion(int x){
        if(x == 1){
            return 0;
        }
        if(cache[x] != 0) return cache[x];
        int a = Integer.MAX_VALUE, b = Integer.MAX_VALUE, c = Integer.MAX_VALUE, d = Integer.MAX_VALUE;
        if(x % 5 == 0){
            a = recursion(x / 5);
        }
        if(x % 3 == 0){
            b = recursion(x / 3);
        }
        if(x % 2 == 0){
            c = recursion(x / 2);
        }
        d = recursion(x - 1);
        return cache[x] = 1 + Math.min(Math.min(a, b), Math.min(c, d));
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int x = Integer.parseInt(br.readLine());
        cache = new int[x + 1];
        bw.write(recursion(x) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
26
 */


 */

/*
26
 */

