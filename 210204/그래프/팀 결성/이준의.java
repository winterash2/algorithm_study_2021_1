package graph;

import java.util.Scanner;

public class 팀결성 {
    static int n, m;
    static int[] p;

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if(a < b){
            p[b] = a;
        } else {
            p[a] = b;
        }
    }

    static int find(int x){
        if(p[x] != x){
            return p[x] = find(p[x]);
        }
        return p[x];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        p = new int[n + 1];
        for(int i = 1; i < n + 1; ++i){
            p[i] = i;
        }
        for(int i = 0; i < m; ++i){
            int oper = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(oper == 0){
                union(a, b);
            } else {
                if(find(a) == find(b)){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
    }
}
