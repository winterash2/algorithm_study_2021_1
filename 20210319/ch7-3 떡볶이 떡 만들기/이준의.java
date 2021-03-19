package binarysearch;

import java.util.*;
import java.io.*;

public class 복습_떡볶이떡만들기 {

    static int n, m;
    static int[] arr;

    static int cut(int h){
        int sum = 0;
        for(int i = 0; i < n; ++i){
            int remain = arr[i] - h;
            if(remain > 0){
                sum += remain;
            }
        }
        return sum;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; ++i){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int answer = 0;
        int left = 0, right = 2000000000;
        while(left <= right){
            int mid = (left + right) / 2;
            if(cut(mid) >= m){
                if(mid > answer) answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
4 6
19 15 10 17
 */
