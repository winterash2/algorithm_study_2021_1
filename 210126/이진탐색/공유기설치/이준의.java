package binarysearch;

import java.util.Arrays;
import java.util.Scanner;

public class 공유기설치 {
    public static int calc(int mid, int[] arr){
        int cnt = 1;
        long cur = arr[0];
        for(int i = 0; i < arr.length; ++i){
            if(arr[i] - cur >= mid){
                cnt++;
                cur = arr[i];
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int c = sc.nextInt();
        int[] arr = new int[n];
        int left = 0, right = 0;
        for(int i = 0; i < n; ++i){
            arr[i] = sc.nextInt();
            if(right < arr[i]) right = arr[i];
        }
        Arrays.sort(arr);
        int answer = 0;
        while(left <= right){
            int mid = (int) (left + right) / 2;
            // 공유기가 많이 설치 됐다는 것은 현재보다 더 긴 거리를 두어서 설치할 수 있다
            if(calc(mid, arr) >= c){
                left = mid + 1;
                answer = mid;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }
}
