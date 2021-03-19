package simulation;

import java.util.*;
import java.io.*;


// 얘는 bfs 할때 큐에 넣을때만
class Coord{
    int x, y;
    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 복습_게임개발 {

    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static boolean[][] visit;
    static int[][] map;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int cx = Integer.parseInt(st.nextToken());
        int cy = Integer.parseInt(st.nextToken());
        int direc = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visit = new boolean[n][m];
        for(int i = 0; i < n; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; ++j){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int answer = 1;
        boolean check = true;
        visit[cx][cy] = true;
        while(true){
            for(int i = 0; i < 4; ++i){
                // 0 -> 3 -> 2 -> 1 -> 0
                direc = direc - 1 < 0 ? 3 : direc - 1;
                if(i == 3){
                    // 4번째 돌았을때
                    int nx = cx - dx[direc];
                    int ny = cy - dy[direc];
                    if(map[nx][ny] == 1){
                        check = false;
                        break;
                    } else {
                        cx = nx;
                        cy = ny;
                        continue;
                    }
                }
                int nx = cx + dx[direc];
                int ny = cy + dy[direc];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && map[nx][ny] == 0){
                    cx = nx;
                    cy = ny;
                    visit[nx][ny] = true;
                    answer++;
                    break;
                }
            }
            if(!check) break;
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
 */

