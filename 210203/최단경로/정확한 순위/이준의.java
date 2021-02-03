package shortestpath2;

import java.util.Scanner;
import java.util.stream.DoubleStream;

public class 정확한순위 {
    static int n, m;
    static int[][] graph;
    static final int INF = (int) 1e9;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        graph = new int[n + 1][n + 1];
        for(int i = 0; i < n + 1; ++i){
            for(int j = 0; j < n + 1; ++j){
                graph[i][j] = INF;
                if(i == j) graph[i][j] = 0;
            }
        }

        for(int i = 0; i < m; ++i){
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = 1;
        }

        for(int k = 1; k < n + 1; ++k){
            for(int a = 1; a < n + 1; ++a){
                for(int b = 1; b < n + 1; ++b){
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }

        int answer = 0;
        for(int i = 1; i < n + 1; ++i){
            int count = 0;
            for(int j = 1; j < n + 1; ++j){
                if(graph[j][i] != INF || graph[i][j] != INF) count++;
            }
            if(n == count) answer++;
        }
        System.out.println(answer);
    }
}
/*
6 6
1 5
3 4
4 2
4 6
5 2
5 4
 */