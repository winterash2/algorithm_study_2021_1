package dfsbfs;

import java.util.*;
import java.io.*;


class Coord{
    int x, y;
    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 복습_음료수얼려먹기 {

    static int[][] map;
    static boolean[][] visit;
    static int answer = 0;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};
    static int n, m;

    static void bfs(Coord start){
        Queue<Coord> q = new LinkedList<>();
        q.offer(start);
        visit[start.x][start.y] = true;

        while(!q.isEmpty()){
            Coord cur = q.poll();
            for(int i = 0; i < 4; ++i){
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && map[nx][ny] == 0){
                    visit[nx][ny] = true;
                    q.offer(new Coord(nx, ny));
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visit = new boolean[n][m];
        map = new int[n][m];
        for(int i = 0; i < n; ++i){
            String input = br.readLine();
            for(int j = 0; j < m; ++j){
                map[i][j] = input.charAt(j) - '0';
            }
        }

        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                if(!visit[i][j] && map[i][j] == 0){
                    bfs(new Coord(i, j));
                    answer++;
                }
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
4 5
00110
00011
11111
00000

4 5
00111
11011
11101
10111


11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
 */

