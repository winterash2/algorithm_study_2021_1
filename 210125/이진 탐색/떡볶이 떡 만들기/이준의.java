package binarysearch;

import java.util.Arrays;

public class 떡볶이떡만들기 {
    public static int cut(int mid, int[] arr){
        int ret = 0;
        for(int i = 0; i < arr.length; ++i){
            if(arr[i] > mid) ret += arr[i] - mid;
        }
        return ret;
    }

    public static void main(String[] args) {
        int n = 4, m = 6;
        int[] arr = {19, 15, 10, 17};
        int answer = 0;
        Arrays.sort(arr);
        int left = arr[0], right = arr[n - 1];

        while(left <= right){
            int mid = (int) (left + right) / 2;
            int sum = cut(mid, arr);
            if(sum >= m){
                answer = mid;
                left = mid + 1;
            } else if(sum < m){
                right = mid - 1;
            }
        }
        System.out.println(answer);
    }
}
