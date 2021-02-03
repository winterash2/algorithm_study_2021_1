package shortestpath;

import java.util.Scanner;
/*
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
 */

/*
4 2
1 3
2 4
3 4
 */
public class 미래도시 {

    static int n, m, x, k;
    static int[][] graph;
    static final int INF = (int) 1e9;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        graph = new int[n + 1][n + 1];
        for(int i = 1; i < n + 1; ++i){
            for(int j = 1; j < n + 1; ++j){
                graph[i][j] = INF;
                if(i == j) graph[i][j] = 0;
            }
        }
        for(int i = 0; i < m; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        x = sc.nextInt();
        k = sc.nextInt();

        for(int i = 1; i < n + 1; ++i){
            for(int a = 1; a < n + 1; ++a){
                for(int b = 1; b < n + 1; ++b){
                    graph[a][b] = Math.min(graph[a][b], graph[a][i] + graph[i][b]);
                }
            }
        }

        if(graph[1][k] + graph[k][x] >= INF){
            System.out.println("-1");
        } else {
            System.out.println(graph[1][k] + graph[k][x]);
        }

    }
}
