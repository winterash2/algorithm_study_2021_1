package greedy;

import java.util.*;
import java.io.*;

public class 큰수의법칙 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];

        for(int i = 0; i < n; ++i){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);
        int answer = 0;
        if(arr[n - 1] == arr[n - 2]){
            answer = m * arr[n - 1];
        } else {
            int mod = m % k;
            int div = m / k;
            answer = div * arr[n - 1] * k + mod * arr[n - 2];
        }

        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
5 8 3
2 4 5 4 6

3 5 3
2 3 3
 */

