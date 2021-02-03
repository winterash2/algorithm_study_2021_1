package shortestpath2;

import java.util.PriorityQueue;
import java.util.Scanner;

class Mars implements Comparable<Mars>{
    int i, j;
    int cost;
    public Mars(int i, int j, int cost){
        this.i = i;
        this.j = j;
        this.cost = cost;
    }

    @Override
    public int compareTo(Mars o) {
        return this.cost - o.cost;
    }
}

public class 화성탐사 {

    static int t, n;
    static int[][] graph;
    static int[][] distance;
    static PriorityQueue<Mars> q;

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, 1, -1};

    static final int INF = (int) 1e9;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for(int testCase = 0; testCase < t; ++testCase){
            n = sc.nextInt();
            graph = new int[n + 1][n + 1];
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < n; ++j){
                    graph[i][j] = sc.nextInt();
                }
            }

            distance = new int[n + 1][n + 1];
            for(int i = 0; i < n + 1; ++i){
                for(int j = 0; j < n + 1; ++j){
                    distance[i][j] = INF;
                }
            }

            distance[0][0] = graph[0][0];
            q = new PriorityQueue<Mars>();
            q.offer(new Mars(0, 0, graph[0][0]));
            while(!q.isEmpty()){
                Mars cur = q.poll();
                int dist = cur.cost;
                int x = cur.i;
                int y = cur.j;
                if(distance[x][y] < dist) continue;
                for(int i = 0 ; i < 4; ++i){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(0 <= nx && nx < n && 0 <= ny && ny < n){
                        int cost = dist + graph[nx][ny];
                        if(cost < distance[nx][ny]){
                            distance[nx][ny] = cost;
                            q.offer(new Mars(nx, ny, cost));
                        }
                    }
                }
            }

            System.out.println(distance[n - 1][n - 1]);
        }
    }
}

/*
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
 */