package dp;

import java.util.*;
import java.io.*;

public class 복습_1로만들기 {

    static int recursion(int x){
        if(x == 1){
            return 0;
        }
        int a = Integer.MAX_VALUE, b = Integer.MAX_VALUE, c = Integer.MAX_VALUE, d = Integer.MAX_VALUE;
        if(x % 5 == 0){
            a = recursion(x / 5);
        }
        if(x % 3 == 0){
            b = recursion(x / 3);
        }
        if(x % 3 == 0){
            c = recursion(x / 2);
        }
        d = recursion(x - 1);
        return 1 + Math.min(Math.min(a, b), Math.min(c, d));
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int x = Integer.parseInt(br.readLine());
        bw.write(recursion(x) + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
26
 */

