package simulation;

import java.util.*;
import java.io.*;

public class 복습_왕실의나이트 {

    static int[] dx = {-1, -2, -2, -1, 1, 2, 2, 1};
    static int[] dy = {2, 1, -1, -2, -2, -1, 1, 2};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        int answer = 0;
        int row = input.charAt(0) - 'a';
        int col = input.charAt(1) - '0' - 1;
        for(int i = 0; i < 8; ++i){
            int nx = row + dx[i];
            int ny = col + dy[i];
            if(0 <= nx && nx < 8 && 0 <= ny && ny < 8){
                answer++;
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
a1  -> 2
b4  -> 6
 */
