package greedy;

import java.util.Arrays;
import java.util.Scanner;

public class 통나무건너뛰기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testCase = sc.nextInt();
        for(int t = 0; t < testCase; ++t){
            int n = sc.nextInt();
            int[] arr = new int[n];
            int[] minArr = new int[n];
            int answer = 0;
            int left = 0, right = n - 1;
            for(int i = 0; i < n; ++i){
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);

            for(int i = 0; i < n; ++i){
                if(i % 2 == 0){
                    minArr[left++] = arr[i];
                } else {
                    minArr[right--] = arr[i];
                }
            }

            for(int i = 0; i < n; ++i){
                int diff = 0;
                if(i == n - 1){
                    diff = Math.abs(minArr[0] - minArr[i]);
                } else {
                    diff = Math.abs(minArr[i + 1] - minArr[i]);
                }
                if(diff > answer){
                    answer = diff;
                }
            }
            System.out.println(answer);
        }
    }
}


/*
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
 */