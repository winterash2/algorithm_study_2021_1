package 정렬;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 두배열의원소교체 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        ArrayList<Integer> arrA = new ArrayList<>();
        ArrayList<Integer> arrB = new ArrayList<>();
        ArrayList<Integer> arrAnswer = new ArrayList<>();
        for(int i=0; i<N; i++){
            arrA.add(sc.nextInt());
        }
        for(int i=0; i<N; i++){
            arrB.add(sc.nextInt());
        }
        Collections.sort(arrA, Collections.reverseOrder());
        int answer = 0;
        for(int i=0; i<N-K; i++){
            answer += arrA.get(i);
        }
        for(int i=N-K; i<N; i++){
            arrB.add(arrA.get(i));
        }
        Collections.sort(arrB, Collections.reverseOrder());
        for(int i=0; i<K; i++){
            answer += arrB.get(i);
        }
        System.out.println(answer);
    }
}
/*
5 3
1 2 5 4 3
5 5 6 6 5
 */