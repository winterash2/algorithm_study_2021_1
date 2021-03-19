package greedy;

import java.util.*;
import java.io.*;

public class 복습_1이될때까지 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int answer = 0;
        while(n != 1){
            if(n % k == 0){
                n /= k;
            } else {
                n -= 1;
            }
            answer++;
        }
        bw.write(answer + " \n");
        bw.flush();
        bw.close();
        br.close();
    }
}
/*
25 5
 */