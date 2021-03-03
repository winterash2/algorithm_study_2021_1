package simulation;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Dust{
    int amount, x, y;
    public Dust(int amount, int x, int y) {
        this.amount = amount;
        this.x = x;
        this.y = y;
    }
}

public class 미세먼지안녕 {

    static int[][] map;
    static int r;
    static int c;
    static int t;
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int puryX1, puryX2, puryY1, puryY2;

    static void spread() {
        Queue<Dust> q = new LinkedList<>();
        for(int i = 0; i < r; ++i){
            for(int j = 0; j < c; ++j){
                if(map[i][j] != 0 && map[i][j] != -1){
                    q.offer(new Dust(map[i][j], i, j));
                }
            }
        }
        int size = q.size();
        for(int i = 0; i < size; ++i){
            Dust now = q.poll();
            int spreadAmount = now.amount / 5;
            int spreadCount = 0;
            for(int k = 0; k < 4; ++k){
                int nx = now.x + dx[k];
                int ny = now.y + dy[k];
                if(0 <= nx && nx < r && 0 <= ny && ny < c && map[nx][ny] != -1){
                    spreadCount++;
                    map[nx][ny] += spreadAmount;
                }
            }
            map[now.x][now.y] -= spreadAmount * spreadCount;
        }
    }

    static void clean() {
        int tmp = map[puryX1][c - 1];
        for(int i = c - 1; i > 1; --i){
            map[puryX1][i] = map[puryX1][i - 1];
        }
        map[puryX1][1] = 0;
        int tmp2 = map[0][c - 1];
        for(int i = 0; i < puryX1 - 1; ++i){
            map[i][c - 1] = map[i + 1][c - 1];
        }
        map[puryX1 - 1][c - 1] = tmp;
        tmp = map[0][0];
        for(int i = 0; i < c - 1; ++i){
            map[0][i] = map[0][i + 1];
        }
        map[0][c - 2] = tmp2;

        for(int i = puryX1 - 1; i > 1; --i){
            map[i][0] = map[i - 1][0];
        }
        map[1][0] = tmp;

        tmp = map[puryX2][c - 1];
        for(int i = c - 1; i > 1; --i){
            map[puryX2][i] = map[puryX2][i - 1];
        }
        map[puryX2][1] = 0;
        tmp2 = map[r - 1][c - 1];
        for(int i = r - 1; i > puryX2 + 1; --i){
            map[i][c - 1] = map[i - 1][c - 1];
        }
        map[puryX2 + 1][c - 1] = tmp;
        tmp = map[r - 1][0];
        for(int i = 0; i < c - 1; ++i){
            map[r - 1][i] = map[r - 1][i + 1];
        }
        map[r - 1][c - 2] = tmp2;
        for(int i = puryX2 + 1; i < r - 1; ++i){
            map[i][0] = map[i + 1][0];
        }
        map[r - 2][0] = tmp;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());
        map = new int[r][c];
        int cnt = 0;

        for(int i = 0; i < r; ++i){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < c; ++j){
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == -1 && cnt == 0){
                    puryX1 = i;
                    puryY1 = j;
                    cnt++;
                }
                if(map[i][j] == -1 && cnt == 1){
                    puryX2 = i;
                    puryY2 = j;
                }
            }
        }

        for(int i = 0; i < t; ++i){
            spread();
            clean();
        }

        int answer = 0;
        for(int i = 0; i < r; ++i){
            for(int j = 0; j < c; ++j){
                if(map[i][j] != -1){
                    answer += map[i][j];
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
7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0
 */
