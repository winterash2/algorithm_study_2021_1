package dfsbfs2;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Point{
    int x, y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 아기상어2 {

    static int[][] map;
    static boolean[][] visit;
    static int n, m;

    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    static int bfs(int x, int y){
        int distance = 0;
        Queue<Point> q = new LinkedList<>();
        q.offer(new Point(x, y));
        visit[x][y] = true;
        boolean check = false;
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; ++i){
                Point cur = q.poll();
                int cx = cur.x;
                int cy = cur.y;
                if(map[cx][cy] == 1) {
                    check = true;
                    break;
                }
                for(int j = 0; j < 8; ++j){
                    int nx = cx + dx[j];
                    int ny = cy + dy[j];
                    if(0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny]){
                        visit[nx][ny] = true;
                        q.offer(new Point(nx, ny));
                    }
                }
            }
            if(check) break;
            distance++;
        }
        return distance;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        map = new int[n][m];
        visit = new boolean[n][m];
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                map[i][j] = sc.nextInt();
            }
        }
        int maxVal = (int) -1e9;
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(map[i][j] == 0){
                    int ret = bfs(i, j);
                    visit = new boolean[n][m];
                    if(ret > maxVal) maxVal = ret;
                }
            }
        }

        System.out.println(maxVal);
    }
}

/*
5 4
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
 */
