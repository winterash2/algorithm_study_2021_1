package dfsbfs2;

import javax.sound.midi.SysexMessage;
import java.util.*;
import java.io.*;

class Node{
    int x,y;

    public Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class 벽부수고이동하기 {

    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] map = new int[n][m];
        boolean[][] visit = new boolean[n][m];
        for(int i = 0; i < n; ++i){
            String input = br.readLine();
            for(int j = 0; j < input.length(); ++j){
                map[i][j] = input.charAt(j) - '0';
            }
        }

        int answer = 2000000;

        for(int i = 0; i < n; ++i){
            for(int j = 0 ; j < m; ++j){
                if(map[i][j] == 1){
                    map[i][j] = 0;
                    Queue<Node> q = new LinkedList<>();
                    visit = new boolean[n][m];
                    q.offer(new Node(0, 0));
                    visit[0][0] = true;
                    int cnt = 0;
                    while(!q.isEmpty()){
                        int size = q.size();
                        for(int iter = 0; iter < size; ++iter){
                            int x = q.peek().x;
                            int y = q.peek().y;
                            q.poll();
                            if(x == n - 1 && y == m - 1){
                                if(answer > cnt){
                                    answer = cnt + 1;
                                }
                            }
                            for(int k = 0; k < 4; ++k){
                                int nx = x + dx[k];
                                int ny = y + dy[k];
                                if(0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && map[nx][ny] == 0){
                                    q.offer(new Node(nx, ny));
                                    visit[nx][ny] = true;
                                }
                            }
                        }
                        cnt++;
                    }
                    map[i][j] = 1;
                }
            }
        }
        if(answer == 2000000){
            bw.write(-1 + "\n");
        } else {
            bw.write(answer +"\n");
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
6 4
0100
1110
1000
0000
0111
0000
 */

