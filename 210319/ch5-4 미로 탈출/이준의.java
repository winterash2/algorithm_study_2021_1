package dfsbfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class 복습_미로탈출 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 한 번 bfs 수행할 경우에는 main 안에
        // 여러번 bfs 수행할 경우에는 main 밖에

        // 1이 빈칸, 0이 괴물이고 시작 위치는 1, 1인데 0, 0 에서 시작해도 상관없음
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][m];
        boolean[][] visit = new boolean[n][m];
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        for (int i = 0; i < n; ++i) {
            String input = br.readLine();
            for (int j = 0; j < m; ++j) {
                map[i][j] = input.charAt(j) - '0';
            }
        }
        Queue<Coord> q = new LinkedList<>();
        q.offer(new Coord(0, 0));
        visit[0][0] = true;
        int answer = 0;
        boolean check = false;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                Coord cur = q.poll();
                if (cur.x == n - 1 && cur.y == m - 1) {
                    check = true;
                    break;
                }
                for (int j = 0; j < 4; ++j) {
                    int nx = cur.x + dx[j];
                    int ny = cur.y + dy[j];
                    if (0 <= nx && nx < n && 0 <= ny && ny < m && !visit[nx][ny] && map[nx][ny] == 1) {
                        visit[nx][ny] = true;
                        q.offer(new Coord(nx, ny));
                    }
                }

            }
            answer++;
            if (check) {
                break;
            }
        }
        bw.write(answer + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
}

/*
5 6
101010
111111
000001
111111
111111

6 6
101010
111111
000001
111111
111110
111111
 */
