package binarysearch;

import java.util.Arrays;

public class 부품찾기 {
    public static void main(String[] args) {
        int n = 5;
        int[] arr1 = {8, 3, 7, 9, 2};
        int m = 2;
        int[] arr2 = {7, 9};

        Arrays.sort(arr1);

        for(int i = 0; i < m; ++i){
            int left = 0;
            int right = n - 1;
            boolean check = false;
            while(left <= right){
                int mid = (int) (left + right) / 2;
                if(arr1[mid] > arr2[i]){
                    right = mid - 1;
                } else if(arr1[mid] < arr2[i]){
                    left = mid + 1;
                }else {
                    check = true;
                    break;
                }
            }
            if(!check) {
                System.out.println("no");
                return;
            }
            check = false;
        }
        System.out.println("yes");
    }
}
