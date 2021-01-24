package sort;

import java.util.Arrays;
import java.util.Scanner;

public class 안테나 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; ++i){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        int answer = n % 2 == 0 ? arr[n / 2 - 1] : arr[(int) n/ 2];
        System.out.println(answer);
    }
}
