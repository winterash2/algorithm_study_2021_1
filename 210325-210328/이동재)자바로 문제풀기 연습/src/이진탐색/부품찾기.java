package 이진탐색;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 부품찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> arrA = new ArrayList<>();
        for(int i=0; i<N; i++){
            arrA.add(sc.nextInt());
        }
        int M = sc.nextInt();
        int[] arrB = new int[M];
        for(int i=0; i<M; i++){
            arrB[i] = sc.nextInt();
        }
        Collections.sort(arrA);
        for(int i=0; i<arrB.length; i++){
            int result = Collections.binarySearch(arrA, arrB[i]);
            if(result < 0){
                System.out.print("no ");
            }else{
                System.out.print("yes ");
            }
        }
    }
}
/*
5
8 3 7 9 2
3
5 7 9
 */