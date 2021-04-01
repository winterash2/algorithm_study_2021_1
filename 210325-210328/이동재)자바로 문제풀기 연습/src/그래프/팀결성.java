package 그래프;

import java.util.Scanner;

public class 팀결성 {
    public static int N;
    public static int M;

    public static int find(int[] parent, int x){
        if(parent[x] != x){
            parent[x] = find(parent, parent[x]);
        }
        return parent[x];
    }
    public static void union(int[] parent, int a, int b) {
        a = find(parent, a);
        b = find(parent, b);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        int[] parent = new int[N+1];
        for (int i = 0; i < N + 1; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            int inst = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(inst == 0){
                union(parent, a, b);
            }else{
                if (find(parent, a) == find(parent, b)) {
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }
    }
}
/*
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
 */
