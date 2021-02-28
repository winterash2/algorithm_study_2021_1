package kmp;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class 찾기 {

    static int[] makeTable(String pattern){
        int patternSize = pattern.length();
        int[] table = new int[patternSize];
        int j = 0;
        for(int i = 1; i < patternSize; ++i){
            while(j > 0 && pattern.charAt(i) != pattern.charAt(j)){
                j = table[j - 1];
            }
            if(pattern.charAt(i) == pattern.charAt(j)){
                table[i] = ++j;
            }
        }
        return table;
    }

    static ArrayList<Integer> kmp(String input, String pattern){
        ArrayList<Integer> ret = new ArrayList<>();
        int[] table = makeTable(pattern);
        int inputSize = input.length();
        int patternSize = pattern.length();
        int j = 0;
        for(int i = 0; i < inputSize; ++i){
            while(j > 0 && input.charAt(i) != pattern.charAt(j)){
                j = table[j - 1];
            }
            if(input.charAt(i) == pattern.charAt(j)){
                if(j == patternSize - 1){
                    ret.add(i - patternSize + 2);
                    j = table[j];
                } else {
                    j++;
                }
            }
        }
        return ret;
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = br.readLine();
        String pattern = br.readLine();
        ArrayList<Integer> answer = kmp(input, pattern);
        bw.write(answer.size() + "\n");
        for(int i = 0; i < answer.size(); ++i){
            bw.write(answer.get(i) + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
ABC ABCDAB ABCDABCDABDE
ABCDABD
 */

// https://www.youtube.com/watch?v=yWWbLrV4PZ8   <- 갓동빈 설명