package dfsbfs2;

import java.util.*;
import java.io.*;

class Location{
    int x, y;
    public Location(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 열쇠 {

    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};
    static boolean[] key = new boolean[26];
    static boolean[][] visit;


    // 오른쪽, 아래, 왼쪽, 위
    static int[] direcX = {0, 1, 0, -1};
    static int[] direcY = {1, 0, -1, 0};
    static int[] iter = new int[4];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int t = Integer.parseInt(st.nextToken());
        for(int testCase = 0; testCase < t; ++testCase){
            int answer = 0;

            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            iter[0] = m - 1;
            iter[1] = n - 1;
            iter[2] = m - 1;
            iter[3] = n - 1;

            // 지도 입력받기
            char[][] map = new char[n][m];
            visit = new boolean[n][m];
            for(int i = 0; i < n; ++i){
                String input = br.readLine();
                for(int j = 0; j < m; ++j){
                    map[i][j] = input.charAt(j);
                }
            }

            // 열쇠 입력받기
            String keys = br.readLine();
            for(int i = 0; i < keys.length(); ++i){
                if(keys.charAt(i) =='0') break;
                key[keys.charAt(i) - 'a'] = true;
            }

            int enterX = 0;
            int enterY = 0;
            // 진입로 찾기
            for(int k = 0; k < 4; ++k){
                // 오른쪽 m칸, 아래쪽 n 칸, 왼쪽 m칸, 위쪽 n칸 이동
                boolean check = false;
                for(int i = 0; i < iter[k]; ++i){
                    enterX += direcX[k];
                    enterY += direcY[k];

                    if(map[enterX][enterY] != '*'){
                        Queue<Location> q = new LinkedList<>();
                        if(Character.isAlphabetic(map[enterX][enterY]) && key[Character.toLowerCase(map[enterX][enterY]) - 'a']){
                            q.offer(new Location(enterX, enterY));
                            visit[enterX][enterY] = true;
                        } else if(map[enterX][enterY] == '.'){
                            q.offer(new Location(enterX, enterY));
                            visit[enterX][enterY] = true;
                        }
                        // 열쇠인 경우가 있을수 있음

                        while(!q.isEmpty()){
                            Location cur = q.poll();
                            for(int j = 0; j < 4; ++j){
                                int nx = cur.x + dx[j];
                                int ny = cur.y + dy[j];
                                if(0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && map[nx][ny] != '*'){
                                    if(Character.isLowerCase(map[nx][ny])){
                                        key[map[nx][ny] - 'a'] = true;
                                        // 다른 문을 열 수 있는 가능성이 생겼으니 방문체크 초기화 및 다른 진입점 탐색해보기
                                        map[nx][ny] = '.';
                                        visit = new boolean[n][m];
                                        check = true;
                                        visit[nx][ny] = true;
                                        q.offer(new Location(nx, ny));
                                    } else if(Character.isAlphabetic(map[nx][ny]) && key[Character.toLowerCase(map[nx][ny]) - 'a']){
                                        map[nx][ny] = '.';
                                        visit[nx][ny] = true;
                                        q.offer(new Location(nx, ny));
                                    } else if(map[nx][ny] == '$'){
                                        map[nx][ny] = '.';
                                        visit[nx][ny] = true;
                                        answer++;
                                        q.offer(new Location(nx, ny));
                                    } else if(map[nx][ny] == '.'){
                                        visit[nx][ny] = true;
                                        q.offer(new Location(nx, ny));
                                    }
                                }
                            }
                        }
                    }
                }
                if(check) {
                    enterX = 0;
                    enterY = 0;
                    k = -1;
                    continue;
                }
            }
            bw.write(answer + "\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
/*
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony
 */

