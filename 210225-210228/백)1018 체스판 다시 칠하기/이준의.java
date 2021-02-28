package bruteforce;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 체스판다시칠하기 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] chess = new char[n][m];
        for(int i = 0; i < n; ++i){
            String input = br.readLine();
            for(int j = 0; j < m; ++j){
                chess[i][j] = input.charAt(j);
            }
        }

        int min = Integer.MAX_VALUE;
        for(int i = 0; i < n - 7; ++i){
            for(int j = 0; j < m - 7; ++j){
                int cntB = 0;
                int cntW = 0;
                for(int a = i; a < i + 8; ++a){
                    for(int b = j; b < j + 8; ++b){
                        if((a + b) % 2 == 0){
                            if(chess[a][b] == 'B')
                                cntW++;
                            else
                                cntB++;
                        } else {
                            if(chess[a][b] == 'B')
                                cntB++;
                            else
                                cntW++;
                        }
                    }
                }
                min = Math.min(min, cntB);
                min = Math.min(min, cntW);
            }
        }

        bw.write(min + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
 */
