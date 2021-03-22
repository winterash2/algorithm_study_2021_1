package greedy;

import java.util.*;
import java.io.*;

public class 숫자카드게임 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] arr = new int[n][m];

        for(int i = 0; i < n; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; ++j){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int minValue = Integer.MAX_VALUE;
        int answer = Integer.MIN_VALUE;

        for(int i = 0; i < n; ++i){
            minValue = Integer.MAX_VALUE;
            for(int j = 0; j < m; ++j){
                if(arr[i][j] < minValue) minValue = arr[i][j];
            }
            if(answer < minValue) answer = minValue;
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}


// 큰 것 중 작은 것 찾기

/*
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
 */

