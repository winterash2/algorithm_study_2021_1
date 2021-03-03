package dfsbfs2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 유기농배추 {

    static int cnt;
    static boolean[][] check = new boolean[51][51];
    static int[][] map = new int[51][51];
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};

    static int n, m, k, t;


    static void dfs(int x, int y){
        check[x][y] = true;
        for(int i = 0; i < 4; ++i){
            int nx = x + dx[i];
            int ny = y + dy[i];
            if(0 <= nx && nx < n && 0 <= ny && ny < m && !check[nx][ny] && map[nx][ny] == 1){
                dfs(nx, ny);
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());
        while(t != 0){
            map = new int[51][51];
            check = new boolean[51][51];
            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());
            for(int i = 0; i < k; ++i){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                map[y][x] = 1;
            }
            for(int i = 0; i < n; ++i){
                for(int j = 0; j < m; ++j){
                    if(!check[i][j] && map[i][j] == 1){
                        dfs(i, j);
                        cnt++;
                    }
                }
            }
            bw.write(cnt + "\n");
            cnt = 0;
            t--;
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
