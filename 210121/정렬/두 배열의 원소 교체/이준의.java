package sort;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 두배열의원소교체 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        Integer[] a1 = new Integer[n];
        Integer[] a2 = new Integer[n];
        for(int i = 0; i < n; ++i){
            a1[i] = sc.nextInt();
        }
        for(int i = 0; i < n; ++i){
            a2[i] = sc.nextInt();
        }
        Arrays.sort(a1);
        Arrays.sort(a2, Collections.reverseOrder());
        for(int i = 0; i < k; ++i){
            if(a1[i] < a2[i]){
                a1[i] = a2[i];
            }
        }
        int sum = 0;
        for(int i = 0; i < n; ++i){
            sum += a1[i];
        }
        System.out.println(sum);
    }
}
