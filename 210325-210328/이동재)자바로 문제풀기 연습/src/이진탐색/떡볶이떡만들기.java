package 이진탐색;

import java.util.Scanner;

public class 떡볶이떡만들기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] dducks = new int[N];
        for(int i=0; i<N; i++){
            dducks[i] = sc.nextInt();
        }
        int left = 1;
        int right = 100000000;
        int answer = 0;
        while(left < right){
            int mid = (left + right) / 2;
            int count = 0;
            for(int i=0; i<N; i++){
                int sub = dducks[i] - mid;
                if(sub > 0){
                    count += sub;
                }
            }
            if(count >= M){
                answer = mid;
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }
        System.out.println(answer);
    }
}
/*
4 6
19 15 10 17
 */