package graph2;


import java.util.Scanner;

public class 여행계획 {

    static int n, m;
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
        n = sc.nextInt();
        m = sc.nextInt();
        p = new int[n + 1];
        for(int i = 1; i < n + 1; ++i){
            p[i] = i;
        }
        int[][] arr = new int[n + 1][n + 1];
        for(int i = 1; i < n + 1; ++i){
            for(int j = 1; j < n + 1; ++j){
                arr[i][j] = sc.nextInt();
                if(arr[i][j] == 1){
                    union(i, j);
                }
            }
        }
        for(int i = 1; i < n + 1; ++i){
            find(i);
        }
        boolean check = true;
        int first = sc.nextInt();
        int parent = find(first);
        for(int i = 0; i < m - 1; ++i){
            int city = sc.nextInt();
            if(parent != find(city)){
                System.out.println("NO");
                return;
            }
        }
        System.out.println("YES");
    }
}
/*
5 1
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 1
 */