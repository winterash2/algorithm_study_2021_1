package 최단거리;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class 미래도시 {
    public static final int INF = (int) 1e9;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] graph = new int[N + 1][N + 1];
        for (int i = 0; i < N+1; i++) {
            Arrays.fill(graph[i], INF);
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        int X = sc.nextInt();
        int K = sc.nextInt();

        for (int k = 1; k < N + 1; k++) {
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    graph[i][j] = Integer.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }

        int answer = graph[1][K] + graph[K][X];
        if(answer >= INF) answer = -1;

        System.out.println(answer);
    }
}
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
