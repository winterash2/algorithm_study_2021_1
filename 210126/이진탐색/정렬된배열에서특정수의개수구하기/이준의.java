package binarysearch;

import java.util.Arrays;
import java.util.Random;

public class 정렬된배열에서특정수의개수구하기 {
    public static int[] randomMaker(){
        int[] ret = new int[1000000];
        Random ran = new Random();
        for(int i =0 ; i < 1000000; ++i){
//            ret[i] = (int) (Math.random() * 2 * (int)1e9) - (int)1e9;
            ret[i] = 100;
        }
        return ret;
    }

    public static void main(String[] args) {
//        int n = 7, x = 2;
//        int[] arr = {1, 1, 2, 2, 2, 2, 3};

        int n = 1000000;
        int x = 100;
        int[] arr = randomMaker();
        Arrays.sort(arr);
        int left = 0;
        int right = n - 1;


        // 이진탐색 시간측정

        boolean check = false;
        int leftIndex = 0;
        long start = System.currentTimeMillis();
        while(left <= right){
            int mid = (int) (left + right) / 2;
            if((mid == 0 || arr[mid - 1] < x) && arr[mid] == x){
                leftIndex = mid;
                check = true;
                break;
                // 찾는 값과 같지만 제일 왼쪽 값이 아닐 경우 왼쪽으로 이동
            } else if(arr[mid] >= x){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        left = 0;
        right = n - 1;
        int rightIndex = 0;
        while(left <= right){
            int mid = (int) (left + right) / 2;
            if((mid == n - 1 || arr[mid + 1] > x) && arr[mid] == x){
                rightIndex = mid;
                break;
            } else if(arr[mid] > x){
                right = mid - 1;
                // 찾는 값과 같지만 제일 오른쪽 값이 아닌 경우 오른쪽으로 이동
            } else {
                left = mid + 1;
            }
        }
        long end = System.currentTimeMillis();
        System.out.println("걸린시간1 : " + (end - start) / 1000.0);
        if(!check) {
            System.out.println(-1);
            return;
        }
        System.out.println(rightIndex - leftIndex + 1);


        // 이진탐색으로 값을 찾은후 순차탐

        start = System.currentTimeMillis();
        left = 0;
        right = n - 1;

        leftIndex = 0;
        rightIndex = n - 1;
        while(left <= right){
            int mid = (left + right) / 2;
            if(arr[mid] > x){
                right = mid - 1;
            } else if(arr[mid] < x){
                left = mid + 1;
            } else {
                for(int i = mid - 1; i >= 0; --i){
                    if(arr[i] != x){
                        leftIndex = i;
                        break;
                    }
                }
                for(int i = mid; i <= n - 1; ++i){
                    if(arr[i] != x){
                        rightIndex = i;
                        break;
                    }
                }
            }
            break;
        }
        end = System.currentTimeMillis();
        System.out.println("걸린시간2 : " + (end - start) / 1000.0);

        System.out.println(rightIndex - leftIndex + 1);
    }
}

/*
> Task :정렬된배열에서특정수의개수구하기.main()
걸린시간1 : 0.0
1000000
걸린시간2 : 0.037
1000000

현재 CPU 스케줄 상태에 따라 최소 10배 ~ 50배 가량 속도차이로 이진탐색이 우세함
 */