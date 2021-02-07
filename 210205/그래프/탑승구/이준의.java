package graph2;

import java.util.Scanner;

public class 탑승구3 {
    static int n;
    static int m;
    static int[] p;

    static int find(int x){
        if(x != p[x]){
            return p[x] = find(p[x]);
        }
        return p[x];
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a < b){
            p[b] = a;
        } else {
            p[a] = b;
        }
    }

    static int[] dataGenarator(int n){
        int[] ret = new int[n];
        for(int i = 0; i < n; ++i){
            ret[i] = 100000;
        }
        return ret;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        p = new int[100001];
        for(int i = 0; i < 100001; ++i){
            p[i] = i;
        }
        int[] data = dataGenarator(100000);
        long start = System.currentTimeMillis();
        int answer = 0;
//        for(int i = 0; i < data.length; ++i){
//            if(find(data[i]) != 0){
//                union(find(data[i]), find(data[i]) - 1);
//                answer++;
//            } else {
//                break;
//            }
//        }
//  이 방법은 0.014 ~ 0.032

        for(int i = 0; i < data.length; ++i){
            int j = 0;
            for(j = data[i]; j >= 0; --j){
                if(j == 0) {
                    System.out.println(answer);
                    break;
                }
                if(p[j] != 0){
                    break;
                }
            }
            p[j] = 0;
            answer++;
        }

        long end = System.currentTimeMillis();
        System.out.println(end - start);
        System.out.println(answer);
    }
}

// 이 방법은 4.332 ~ 7.882 정도

/*
100000
100000
100000
100000
100000
....

약 50억번의 연산횟수
 */
