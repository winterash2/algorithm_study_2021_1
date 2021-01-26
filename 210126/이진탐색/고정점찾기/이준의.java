package binarysearch;

import java.util.Scanner;

public class 고정점찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; ++i){
            arr[i] = sc.nextInt();
        }
        int left = 0;
        int right = n - 1;
        while(left <= right){
            int mid = (int) (left + right) / 2;
            if(arr[mid] < mid){
                left = mid + 1;
            } else if(arr[mid] > mid){
                right = mid - 1;
            } else {
                System.out.println(mid);
                return;
            }
        }
        if(left > right){
            System.out.println(-1);
        }
    }
}
