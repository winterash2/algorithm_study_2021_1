package math;

import java.util.ArrayList;
import java.util.Scanner;

public class 제곱ㄴㄴ수 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long minVal = sc.nextLong();
        long maxVal = sc.nextLong();
        long answer = maxVal - minVal + 1;
        boolean[] check = new boolean[(int)(maxVal - minVal + 1)];
        long i = 2;
        while(i * i <= maxVal){
            long sNum = minVal / (i * i);
            if(minVal % (i * i) != 0)
                sNum++;
            while(sNum * (i * i) <= maxVal) {
                if(check[(int) (sNum * (i * i) - minVal)] == false) {
                    check[(int) (sNum * (i * i) - minVal)] = true;
                    answer--;
                }
                sNum++;
            }
            i++;
        }
        System.out.println(answer);
    }
}
