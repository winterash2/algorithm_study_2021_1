package binarysearch;

import java.util.*;
import java.io.*;

public class 복습_부품찾기 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] store = new int[n];
        for(int i = 0; i < n; ++i){
            store[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(store);
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for(int j = 0; j < m; ++j){
            int target = Integer.parseInt(st.nextToken());
            // 이진탐색 코드
            int left = 0;
            int right = n - 1;
            boolean check = false;
            while(left <= right){
                int mid = (left + right) / 2;
                if(store[mid] > target){
                    right = mid - 1;
                } else if(store[mid] < target){
                    left = mid + 1;
                } else {
                    check = true;
                    break;
                }
            }
            if(check){
                bw.write("yes ");
            } else {
                bw.write("no ");
            }
        }
        bw.write("\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
5
8 3 7 9 2
3
5 7 9
 */

