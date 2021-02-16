package unionfind;

import java.util.Scanner;

public class 바이러스 {

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

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        p = new int[n + 1];
        for(int i = 1; i < n + 1; ++i){
            p[i] = i;
        }
        for(int i = 0; i < m; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            union(a, b);
        }

        int answer = 0;
        for(int i = 2; i < n + 1; ++i){
            if(find(i) == 1){
                answer++;
            }
        }
        System.out.println(answer);
    }
}
