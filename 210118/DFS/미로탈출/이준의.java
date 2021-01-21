package dfsbfs;

import java.util.LinkedList;
import java.util.Queue;

class Pair{
    int x;
    int y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
}

public class 미로탈출 {

    private static int n = 5;
    private static int m = 6;
    private static int[][] map = new int[][]{
            {1, 0, 1, 0, 1, 0},
            {1, 1, 1, 1, 1, 1},
            {0, 0, 0, 0, 0, 1},
            {1, 1, 1, 1, 1, 1},
            {1, 1, 1, 1, 1, 1}
    };
    private static int[][] visit = new int[n][m];
    public static final int[] dx = {0, 0, 1, -1};
    public static final int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) {
        Queue<Pair> q = new LinkedList<>();
        q.offer(new Pair(0, 0));
        visit[0][0] = 1;
        int cnt = 0;
        while(!q.isEmpty()){
            int size = q.size();
            Pair cur = q.poll();
            if(cur.x == n - 1 && cur.y == m - 1) {
                break;
            }
            for(int i = 0; i < size; ++i){
                for(int j = 0 ; j < 4; ++j){
                    int nx = cur.x + dx[j];
                    int ny = cur.y + dy[j];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < m && visit[nx][ny] == 0 && map[nx][ny] == 1){
                        visit[nx][ny] = 1;
                        map[nx][ny] = map[cur.x][cur.y] + 1;
                        q.offer(new Pair(nx, ny));
                    }
                }
            }
        }
        System.out.println(map[n - 1][m - 1]);
    }
}
